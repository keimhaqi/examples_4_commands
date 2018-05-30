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

def get_top_product_promo_info_vendor(pool1, pool2, pid):
    sql = "SELECT `product_id`, `vendor_id`, `task_id`, `title_en`, `title_ch`, " \
          " `desc_en`, `desc_ch`, `share_title_en`, `share_title_ch`, `share_desc_en`, `share_desc_ch`, " \
          "`img_url`, `card_width`, `card_height`, `price`, `start_date`, `end_date`, `author_id`, `keywords`, " \
          "`missed_time`, `confirmed`, `created_time`, `confirmed_time`, `deleted_time`, `confirmer_id`" \
          " FROM `top_product_promo_info_vendor` WHERE `product_id`={}".format(pid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    prop = {}
    if cursor.rowcount != 0:
        for (product_id, vendor_id, task_id, title_en, title_ch,
             desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en, share_desc_ch,
             img_url, card_width, card_height, price, start_date, end_date, author_id, keywords,
             missed_time, confirmed, created_time, confirmed_time, deleted_time, confirmer_id
             ) in cursor:
            if product_id is not None:
                prop["id"] = product_id
            if vendor_id is not None:
                prop["vendorId"] = vendor_id
                vendor_logo_url = get_vendor_logo_url(pool1, vendor_id)
                if vendor_logo_url is not None:
                    prop["vendorLogoUrl"] = vendor_logo_url
            if task_id is not None:
                prop["taskId"] = task_id
            if title_en is not None and title_en.strip() != '':
                prop["titleEn"] = title_en
            if title_ch is not None and title_ch.strip() != '':
                prop["titleCh"] = title_ch
            if desc_en is not None and desc_en.strip() != '':
                tmp = html_parser.unescape(desc_en)
                prop["descEn"] = tmp
                # if not tmp.startswith('['):
                #     prop["descEn"] = [html_parser.unescape(desc_en)]
                # else:
                #     prop["descEn"] = tmp[1:-1].replace('"', '').split(',')
            if desc_ch is not None and desc_ch.strip() != '':
                tmp = html_parser.unescape(desc_ch)
                prop["descCh"] = tmp
                # if not tmp.startswith('['):
                #     prop["descCh"] = [html_parser.unescape(desc_ch)]
                # else:
                #     prop["descCh"] = tmp[1:-1].replace('"', '').split(',')
            if share_title_en is not None and share_title_en.strip() != '':
                prop["shareTitleEn"] = share_title_en
            if share_title_ch is not None and share_title_ch.strip() != '':
                prop["shareTitleCh"] = share_title_ch
            if share_desc_en is not None and share_desc_en.strip() != '':
                prop["shareDescEn"] = share_desc_en
            if share_desc_ch is not None and share_desc_ch.strip() != '':
                prop["shareDescCh"] = share_desc_ch
            if img_url is not None and img_url.strip() != '':
                prop["imgUrl"] = img_url
            if card_width is not None and card_width >= 0:
                prop["cardWidth"] = card_width
            if card_height is not None and card_height >= 0:
                prop["cardHeight"] = card_height
            if price is not None:
                if '-' in price:
                    price = price.replace(' ', '')
                    pc = price.split('-')
                    min = None
                    try:
                        min = float(get_only_numbers(pc[0].strip()[1:]))
                    except ValueError, e:
                        logging.error('ProductId=' + str(product_id))
                        logging.error(e)
                        continue
                    max = None
                    try:
                        max = float(get_only_numbers(pc[1].strip()[1:]))
                    except ValueError, e:
                        logging.error('ProductId=' + str(product_id))
                        logging.error(e)
                        continue

                    prop["topPrice"] = {"min": min, "max": max}
                    prop["price"] = price
                elif '~' in price:
                    price = price.replace(' ', '')
                    pc = price.split('~')
                    min = None
                    try:
                        min = float(get_only_numbers(pc[0].strip()[1:]))
                    except ValueError, e:
                        logging.error('ProductId=' + str(product_id))
                        logging.error(e)
                        continue
                    max = None
                    try:
                        max = float(get_only_numbers(pc[1].strip()[1:]))
                    except ValueError, e:
                        logging.error('ProductId=' + str(product_id))
                        logging.error(e)
                        continue
                    prop["topPrice"] = {"min": min, "max": max}
                    prop["price"] = price
                else:
                    min = None
                    try:
                        min = float(get_only_numbers(price[1:]))
                    except ValueError, e:
                        logging.error('ProductId=' + str(product_id))
                        logging.error(e)
                        continue
                    max = None
                    try:
                        max = float(get_only_numbers(price[1:]))
                    except ValueError, e:
                        logging.error('ProductId=' + str(product_id))
                        logging.error(e)
                        continue
                    prop["topPrice"] = {"min": min, "max": max}
                    prop["price"] = price
            if start_date is not None:
                prop["startDate"] = int(time.mktime(time.strptime(str(start_date), '%Y-%m-%d %H:%M:%S')) * 1000)
            if end_date is not None:
                prop["endDate"] = int(time.mktime(time.strptime(str(end_date), '%Y-%m-%d %H:%M:%S')) * 1000)
            if author_id is not None:
                prop["authorId"] = author_id
            if keywords is not None and keywords.strip() != '':
                prop["keywords"] = keywords
            if missed_time is not None:
                prop["missedTime"] = int(time.mktime(time.strptime(str(missed_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if confirmed is not None:
                prop["confirmed"] = str(confirmed)
            if created_time is not None:
                prop["createdTime"] = int(time.mktime(time.strptime(str(created_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if confirmed_time is not None:
                prop["confirmedTime"] = int(time.mktime(time.strptime(str(confirmed_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if deleted_time is not None:
                prop["deletedTime"] = int(time.mktime(time.strptime(str(deleted_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if confirmer_id is not None:
                prop["confirmerId"] = confirmer_id

    cursor.close()
    cnx.close()
    return prop

def get_vendor(pool, vendor_id):
    query_vendor = "SELECT `vendor_id`, `vendor_name_en`, `default_language` FROM `vendor` WHERE `vendor_id`={}".format(
        vendor_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_vendor)
    tmp = None
    for vendor_id, vendor_name_en, default_language in cursor:
        tmp = (vendor_name_en, default_language)

    cursor.close()
    cnx.close()
    return tmp

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

    parser.add_argument('--productUnit', default='5000')
    parser.add_argument('--esHostPort', default='192.168.1.106:9200')
    parser.add_argument('--esCluster', default='elasticsearch')
    parser.add_argument('--esIndex', default='todayspicks')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--docType', default='items')
    parser.add_argument('--attrsType', default='attrs')

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

    es = Elasticsearch(hosts=args.esHostPort, cluster=args.esCluster)
, 
    es_result = helpers.scan(client=es, query={"query":{"match":{"vendors":"amazon"}}},
                             scroll='5m', index=args.esIndex, doc_type=args.docType,
                             timeout="1m")

    final_result = []
    for item in es_result:
        final_result.append(item['_source'])

    topProductPromoInfoVendor = "topProductPromoInfoVendor"
    missedTime = "missedTime"
    productId = "productId"
    t_id = "id"
    vendor_id = "vendorId"
    for item in final_result:
        print(item["productId"])

    pool1.close()
    pool2.close()

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))