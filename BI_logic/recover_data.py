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

def get_vendor_logo_url(pool, vendor_id):
    tmp = None
    if vendor_id is not None:
        query_vendor = "SELECT `vendor_id`, `vendor_logo_url` FROM `vendor` WHERE `vendor_id`={}".format(
            vendor_id)
        cnx = pool.connection()
        cursor = cnx.cursor()
        cursor.execute(query_vendor)
        for vendor_id, vendor_logo_url in cursor:
            tmp = vendor_logo_url

        cursor.close()
        cnx.close()
    return tmp


def price_handler(product_price):
    if product_price is not None and product_price != "" and product_price != 'N/A':
        if '-' in product_price:
            product_price = product_price.replace(' ', '')
            pc = product_price.split('-')
            min = float(get_only_numbers(pc[0].strip()[0:]))
            max = float(get_only_numbers(pc[1].strip()[0:]))
            return {"min": min, "max": max}
        elif '~' in product_price:
            product_price = product_price.replace(' ', '')
            pc = product_price.split('~')
            min = float(get_only_numbers(pc[0].strip()[0:]))
            max = float(get_only_numbers(pc[1].strip()[0:]))
            return {"min": min, "max": max}
        else:
            min = float(get_only_numbers(product_price[0:]))
            max = float(get_only_numbers(product_price[0:]))
            return {"min": min, "max": max}


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


def fix_top_product_promo_info_vendor_history(pool1, pid):
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


            if hid == 5252:
                print(hid)
            if start_date is not None and end_date is not None:
                # if missed_time is not None:
                #     continue
                # else:
                # if end_date == start_date:
                #     delete_record(pool1, hid)
                # delta = end_date - start_date
                # if delta.days == 30:
                delta = end_date - start_date
                if delta.days == 0 and delta.seconds < 5:
                    delete_record(pool1, hid)

                get_data_by_start_date_end_date(pool1, start_date, end_date, hid)
            
            if start_date is not None and missed_time is not None:
                if missed_time < start_date:
                    delete_record(pool1, hid)

            

            if start_date is not None and end_date is None:
                if missed_time is not None:
                    continue
                

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

    parser.add_argument('--dbbackenduser', default='receng')
    parser.add_argument('--dbbackendpassword', default='Rjbd-yihu-75')
    parser.add_argument('--dbbackendhost', default='192.168.1.196')
    parser.add_argument('--dbbackendport', default='3308')
    parser.add_argument('--dbbackenddatabase', default='jinbag_data')

    # parser.add_argument('--dbbackenduser', default='root')
    # parser.add_argument('--dbbackendpassword', default='admin')
    # parser.add_argument('--dbbackendhost', default='localhost')
    # parser.add_argument('--dbbackendport', default='3306')
    # parser.add_argument('--dbbackenddatabase', default='jinbag_data')

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

    # pool2 = PooledDB(
    #     creator=MySQLdb,
    #     host=args.dbbackendhost,
    #     port=int(args.dbbackendport),
    #     user=args.dbbackenduser,
    #     passwd=args.dbbackendpassword,
    #     db=args.dbbackenddatabase,
    #     charset='utf8'
    # )

    product_ids = get_all_may_wrong_data(pool1)
    for pid in product_ids:
        fix_top_product_promo_info_vendor_history(pool1, pid)

    pool1.close()
    # pool2.close()

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))