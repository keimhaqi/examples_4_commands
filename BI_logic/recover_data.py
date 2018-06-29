#!/usr/bin/python
# -*- coding: UTF-8 -*-
from elasticsearch import Elasticsearch
import datetime
import argparse
import MySQLdb
from DBUtils.PooledDB import PooledDB
import logging
import sys
import HTMLParser
import time
import hashlib
from elasticsearch import helpers

reload(sys)
sys.setdefaultencoding('utf-8')

html_parser = HTMLParser.HTMLParser()
hash = hashlib.sha1()


def price_handler(product_price):
    if product_price is not None and product_price != "" and product_price != 'N/A':
        if '-' in product_price:
            return None
        elif '~' in product_price:
            return None
        else:
            min = float(get_only_numbers(product_price[0:]))
            return min


def get_only_numbers(nums):
    ret = ''
    for it in nums:
        if ord(it) >= 48 and ord(it) <= 57:
            ret = ret + it
        if ord(it) == 46:
            ret = ret + it
    if len(ret) == 0:
        ret = '0'
    return ret

def get_info_from_product_sku_amazon(pool2, product_id):
    sql = "SELECT `source_product_id`, `id` FROM `product_sku_amazon` WHERE `product_id`={}".format(product_id)
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    info = {}
    if cursor.rowcount != 0:
        for source_product_id, hid in cursor:
            if source_product_id is not None:
                info["source_product_id"] = source_product_id
            if hid is not None:
                info["id"] = hid
            
            break
    
    cursor.close()
    cnx.close()
    return info
    

def get_history_price_by_primary_key(pool2, hid):
    sql = "SELECT `final_price` FROM `product_amazon_price` WHERE `id`>{} LIMIT 1".format(hid)
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    fin_price = None
    if cursor.rowcount != 0:
        for final_price in cursor:
            if final_price is not None:
                fin_price = final_price
    
    cursor.close()
    cnx.close()
    return fin_price

def get_history_low_price(pool2, source_product_id, vendor_id):
    sql = "SELECT `content` FROM `data_point` WHERE `webpage_id`='{}' AND `domain_id`={}".format(source_product_id, vendor_id)
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    history_low_price = None

    if cursor.rowcount != 0:
        for content in cursor:
            if content is not None:
                history_low_price = content[0]
    
    cursor.close()
    cnx.close()
    return history_low_price





def get_history_price(pool2, id3, date, source_product_id):
    sql = "SELECT `id`, `product_price`, `product_sale`, `final_price` FROM `product_amazon_price` WHERE `product_vendor_id`={} AND `date`='{}'".format(id3, date)
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    history_price = {}

    if cursor.rowcount != 0:
        for hid, product_price, product_sale, final_price in cursor:
            if hid is not None:
                history_price["id"] = hid
            if product_price is not None:
                history_price["product_price"] = product_price
            if product_sale is not None:
                history_price["product_sale"] = product_sale
            if final_price is not None:
                history_price["final_price"] = final_price
    
    cursor.close()
    cnx.close()
    return history_price



def get_all_may_wrong_data(pool1):
    sql = "select * from (select product_id, count(*) as count from top_product_promo_info_vendor_history group by product_id) t where t.count > 1"
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    product_ids = []
    if cursor.rowcount != 0:
        for(product_id, count) in cursor:
            # print("productId = {}, count = {}".format(product_id, count))
            product_ids.append(product_id)
    
    

    cursor.close()
    cnx.close()
    return product_ids

def delete_record(pool, hid):
    sql = "DELETE FROM top_product_promo_info_vendor_history where `id`={}".format(hid)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
    cnx.close()

def delete_record_with_same_start_date(pool, hid, start_date):
    sql = "DELETE FROM top_product_promo_info_vendor_history where `id`>{} and `start_date`='{}'".format(hid, start_date)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
    cnx.close()


def get_data_by_start_date_end_date(pool1, sta_date, en_date, hid):
    sql = "SELECT `id` FROM top_product_promo_info_vendor_history WHERE `start_date`='{}' AND `end_date`='{}' AND `id`>{}".format(sta_date, en_date, hid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    if cursor.rowcount != 0:
        for hid in cursor:
            delete_record(pool1, hid[0])
    
    cursor.close()
    cnx.close()


def update_history_with_new_start_date(pool1, sta_date, hid):
    sql = "UPDATE `top_product_promo_info_vendor_history` SET `start_date`='{}' WHERE `id`={}".format(sta_date, hid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    cnx.commit()
    cursor.close()
    cnx.close()


def get_data_by_start_date(pool1, sta_date, en_date, hid):
    sql = "SELECT `id`, `end_date` FROM top_product_promo_info_vendor_history WHERE `start_date`='{}' AND `id`>{}".format(sta_date, hid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    count = 0

    tmp_end_date = en_date
    if cursor.rowcount != 0:
        for (hidt, end_date) in cursor:
            if end_date is not None:
                if count == 0:
                    update_history_with_new_start_date(pool1, tmp_end_date, hidt)
                else:
                    update_history_with_new_start_date(pool1, tmp_end_date, hidt)
                tmp_end_date = end_date
            count = count + 1
    
    cursor.close()
    cnx.close()
    
    




def fix_top_product_promo_info_vendor_history(pool1, pool2, pid):
    sql = "SELECT `id`, `product_id`, `vendor_id`, `task_id`, `title_en`, `title_ch`, " \
          " `desc_en`, `desc_ch`, `share_title_en`, `share_title_ch`, `share_desc_en`, `share_desc_ch`, " \
          "`img_url`, `card_width`, `card_height`, `price`, `start_date`, `end_date`, `author_id`, `keywords`, " \
          "`missed_time`, `created_time`, `confirmed_time`, `confirmer_id`" \
          " FROM `top_product_promo_info_vendor_history` WHERE `product_id`={} ORDER BY `id` ASC".format(pid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    prop = {}
    if cursor.rowcount != 0:
        for (hid, product_id, vendor_id, task_id, title_en, title_ch,
             desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en, share_desc_ch,
             img_url, card_width, card_height, price, start_date, end_date, author_id, keywords,
             missed_time, created_time, confirmed_time, confirmer_id
             ) in cursor:

            if start_date is not None and end_date is not None:
                delta = end_date - start_date
                if delta.days == 0 and delta.seconds < 5:
                    delete_record(pool1, hid)

                get_data_by_start_date_end_date(pool1, start_date, end_date, hid)
            
            if start_date is not None and missed_time is not None:
                if missed_time < start_date:
                    delete_record(pool1, hid)

            

            if start_date is not None and end_date is not None and missed_time is None:
                delta = end_date - start_date
                if delta.days == 30 and delta.seconds == 0:
                    delete_record(pool1, hid)
            
            if start_date is not None and end_date is not None and confirmer_id != 99:
                delta = end_date - start_date
                if delta.days == 0 and delta.seconds < 180:
                    delete_record(pool1, hid)
            
            if start_date is not None and end_date is not None and confirmer_id != 99:
                get_data_by_start_date(pool1, start_date, end_date, hid)

            
            if start_date is not None and end_date is not None:
                delta = end_date - start_date
                if delta.days > 30:
                    delete_record(pool1, hid)
            
            # if end_date is None and missed_time is None and start_date is not None:
            #     # need to see the price history info of this product
            #     info = get_info_from_product_sku_amazon(pool2, product_id)
            #     if isinstance(info, dict) and len(info) > 0:
            #         keys = info.keys()
            #         if "source_product_id" in keys and "id" in keys:
            #             history_low_price = get_history_low_price(pool2, info["source_product_id"], 3)
            #             history_low_price = price_handler(history_low_price)
                        
            #             history_price = get_history_price(pool2, info["id"], start_date, info["source_product_id"])
            #             if isinstance(history_price, dict) and len(history_price) > 0:
            #                 hp_keys = history_price.keys()
            #                 if "id" in hp_keys:
            #                     specific_history_price = get_history_price_by_primary_key(pool2, history_price["id"])

            #                     if specific_history_price is not None and history_low_price is not None:
            #                         if specific_history_price < history_low_price and "final_price" in hp_keys and specific_history_price < history_price["final_price"]:
            #                             logging.info("It's valid")
            if start_date is not None and end_date is None:
                delete_record_with_same_start_date(pool1, hid, start_date)                               
                

    cursor.close()
    cnx.close()
    return prop


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='repaire_todayspicks_vendors.log', level=logging.DEBUG,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for recommendation engine")
    # parser.add_argument('--vendordbuser', default='receng')
    # parser.add_argument('--vendordbpassword', default='Rjbd-yihu-75')
    # parser.add_argument('--vendordbhost', default='192.168.1.196')
    # parser.add_argument('--vendordbdatabase', default='jinbag')
    # parser.add_argument('--vendordbport', default='3306')

    parser.add_argument('--vendordbuser', default='root')
    parser.add_argument('--vendordbpassword', default='admin')
    parser.add_argument('--vendordbhost', default='localhost')
    parser.add_argument('--vendordbdatabase', default='jinbag')
    parser.add_argument('--vendordbport', default='3306')

    # parser.add_argument('--dbbackenduser', default='receng')
    # parser.add_argument('--dbbackendpassword', default='Rjbd-yihu-75')
    # parser.add_argument('--dbbackendhost', default='192.168.1.196')
    # parser.add_argument('--dbbackendport', default='3308')
    # parser.add_argument('--dbbackenddatabase', default='jinbag_data')

    parser.add_argument('--dbbackenduser', default='root')
    parser.add_argument('--dbbackendpassword', default='admin')
    parser.add_argument('--dbbackendhost', default='localhost')
    parser.add_argument('--dbbackendport', default='3306')
    parser.add_argument('--dbbackenddatabase', default='jinbag_data')

    args = parser.parse_args()

    pool1 = PooledDB(
        creator=MySQLdb,
        host=args.vendordbhost,
        port=int(args.vendordbport),
        user=args.vendordbuser,
        passwd=args.vendordbpassword,
        db=args.vendordbdatabase,
        charset='utf8'
    )

    pool2 = PooledDB(
        creator=MySQLdb,
        host=args.dbbackendhost,
        port=int(args.dbbackendport),
        user=args.dbbackenduser,
        passwd=args.dbbackendpassword,
        db=args.dbbackenddatabase,
        charset='utf8'
    )

    product_ids = get_all_may_wrong_data(pool1)
    for pid in product_ids:
        fix_top_product_promo_info_vendor_history(pool1, pool2, pid)

    pool1.close()
    pool2.close()

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))