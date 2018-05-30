#!/usr/bin/python
# -*- coding: UTF-8 -*-
from elasticsearch import Elasticsearch
from elasticsearch import ElasticsearchException
from elasticsearch import TransportError
import datetime
import argparse
import MySQLdb
from DBUtils.PooledDB import PooledDB
import logging
import sys
import HTMLParser
import simplejson as json
import time
import hashlib
from dateutil import parser as du_parser

reload(sys)
sys.setdefaultencoding('utf-8')

html_parser = HTMLParser.HTMLParser()
hash = hashlib.sha1()


class Price:
    def __init__(self, min, max):
        self.min = min
        self.max = max


def make_action(id, vendor_id):
    action = {"update": {"_id": str(id)}}
    return json.dumps(action)


def make_parent_action(id, vendor_name, product_id):
    action = {"index": {"_id": str(vendor_name + "_" + str(id)), "parent": str(product_id)}}
    return json.dumps(action)


def get_all_product_number(pool):
    """

    :param pool:
    :return: number
    """
    query_product_number = "SELECT count(`product_id`) FROM `product`"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_product_number)
    number = 0
    for (count) in cursor:
        logging.info(count[0])
        number = count[0]
    cursor.close()
    cnx.close()
    logging.info("All = " + str(number))
    return number


def get_brand(pool, brand_id):
    query_brand = "SELECT `brand_name`, `alias_c1`, `alias_c2`,  `alias_e1`, `alias_e2`, `alias_e3`  FROM `brands` WHERE `brand_id`={}".format(
        brand_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_brand)
    ret = ''
    for brand_name, alias_c1, alias_c2, alias_e1, alias_e2, alias_e3 in cursor:
        ret = brand_name
    cursor.close()
    cnx.close()
    return ret


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


def get_all_vendors_tmp(pool, product_id, table_name):
    query_vendor = "SELECT `id` FROM `{}` WHERE `product_id`={}".format(table_name, product_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_vendor)
    if cursor.rowcount != 0:
        cursor.close()
        cnx.close()
        return True

    cursor.close()
    cnx.close()
    return False


# def vendor_handler(pool, product_id):
#     vendors = []
#     if get_all_vendors(pool, product_id, 'product_sku_6pm'):
#         vendors.append(['6pm', 6])
#     if get_all_vendors(pool, product_id, 'product_sku_amazon'):
#         vendors.append(['Amazon', 3])
#     if get_all_vendors(pool, product_id, 'product_sku_amazon_cn'):
#         vendors.append(['Amazon.cn', 5])
#     if get_all_vendors(pool, product_id, 'product_sku_bloomingdales'):
#         vendors.append(['Bloomingdales', 13867])
#     if get_all_vendors(pool, product_id, 'product_sku_macys'):
#         vendors.append(["Macy's", 3184])
#     if get_all_vendors(pool, product_id, 'product_sku_nordstrom'):
#         vendors.append(['Nordstrom', 1237])
#     if get_all_vendors(pool, product_id, 'product_sku_ralphlauren'):
#         vendors.append(['Ralph Lauren', 2])
#     if get_all_vendors(pool, product_id, 'product_sku_saks'):
#         vendors.append(['Saks Fifth Avenue', 13816])
#     if get_all_vendors(pool, product_id, 'product_sku_saksoff'):
#         vendors.append(['Saks Off 5th', 38801])
#     if get_all_vendors(pool, product_id, 'product_sku_striderite'):
#         vendors.append(['Stride Rite', 38655])
#     if get_all_vendors(pool, product_id, 'product_sku_lastcall'):
#         vendors.append(['Neiman Marcus Last Call', 36025])
#     if get_all_vendors(pool, product_id, 'product_sku_walmart'):
#         vendors.append(['Walmart', 2149])

#     return vendors


def get_all_vendors(pool, product_id, es, esIndex, attrType):
    sql = '''
    (SELECT
     id,
     attribute_str,
     13816 AS vendor_id
    FROM product_sku_saks
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        38801 AS vendor_id
    FROM product_sku_saksoff
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        38655 AS vendor_id
    FROM product_sku_striderite
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        13867 AS vendor_id
    FROM product_sku_bloomingdales
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        3184 AS vendor_id
    FROM product_sku_macys
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        1237 AS vendor_id
    FROM product_sku_nordstrom
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        2149 AS vendor_id
    FROM product_sku_walmart
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        2 AS vendor_id
    FROM product_sku_ralphlauren
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        3 AS vendor_id
    FROM product_sku_amazon
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        5 AS vendor_id
    FROM product_sku_amazon_cn
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        6 AS vendor_id
    FROM product_sku_6pm
    WHERE product_id = {})
    UNION ALL
    (SELECT
        id,
        attribute_str,
        36025 AS vendor_id
    FROM product_sku_lastcall
    WHERE product_id = {})
    '''.format(product_id, product_id, product_id, product_id, product_id, product_id, product_id, product_id,
               product_id, product_id, product_id, product_id, )
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    sid = []
    vname = []
    attrs = []
    for (id, attribute_str, vendor_id) in cursor:
        if vendor_id not in sid:
            tmp = None
            sid.append(vendor_id)
            if vendor_id == 6:
                vname.append('6pm')
                tmp = "6pm"
            elif vendor_id == 3:
                vname.append('Amazon')
                tmp = "Amazon"
            elif vendor_id == 5:
                vname.append('Amazon.cn')
                tmp = "Amazon.cn"
            elif vendor_id == 3184:
                vname.append("Macy's")
                tmp = "Macy's"
            elif vendor_id == 1237:
                vname.append("Nordstrom")
                tmp = "Nordstrom"
            elif vendor_id == 2:
                vname.append("Ralph Lauren")
                tmp = "Ralph Lauren"
            elif vendor_id == 13816:
                vname.append("Saks Fifth Avenue")
                tmp = "Saks Fifth Avenue"
            elif vendor_id == 38801:
                vname.append("Saks Off 5th")
                tmp = "Saks Off 5th"
            elif vendor_id == 38655:
                vname.append("Stride Rite")
                tmp = "Stride Rite"
            elif vendor_id == 36025:
                vname.append("Neiman Marcus Last Call")
                tmp = "Neiman Marcus Last Call"
            elif vendor_id == 2149:
                vname.append("Walmart")
                tmp = "Walmart"
            elif vendor_id == 13867:
                vname.append("Bloomingdales")
                tmp = "Bloomingdales"
            elif vendor_id == 38605:
                vname.append("Kohl's")
                tmp = "Kohl's"

            if attribute_str is not None and attribute_str.strip() != '':
                res = json.loads(attribute_str)
                keys = res.keys()
                if "attrs" in keys:
                    for it in res["attrs"]:
                        if "gender" in keys:
                            it["gender"] = res["gender"]
                        if "productType" in keys:
                            it["productType"] = res["productType"]
                        it["id"] = id
                        it["vendors"] = tmp
                        if "price" in it.keys():
                            it["attrsPrice"] = price_handler(it["price"])
                        attrs.append(it)

    cursor.close()
    cnx.close()
    return [sid, vname, attrs]


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


def get_path_info_from_category_tree(pool, cid):
    """

    :param pool:
    :param cid:
    :return: cat_name
    """
    query_category_tree = "SELECT `category_name`, `path` FROM `category_tree` WHERE `category_id`={} ".format(
        cid)
    cnx = pool.connection()
    curs_category_tree = cnx.cursor()
    curs_category_tree.execute(query_category_tree)
    for (category_name, path) in curs_category_tree:
        cat_name = str(html_parser.unescape(category_name)).lower()

    curs_category_tree.close()
    cnx.close()
    return cat_name


def get_category_info_from_category_tree(pool, cid):
    """

    :param pool:
    :param cid:
    :return:
    """
    queryCategoryTree = "SELECT `category_name`, `path` FROM `category_tree` WHERE `category_id`={} ".format(
        cid)
    cnx = pool.connection()
    cursCategoryTree = cnx.cursor()
    cursCategoryTree.execute(queryCategoryTree)
    categories = []
    for (category_name, path) in cursCategoryTree:
        category_name = str(html_parser.unescape(category_name)).lower()
        categories.append(category_name)
        cids = str(path).split('>')
        for cid in cids:
            tmp_cat = get_path_info_from_category_tree(pool, cid)
            if tmp_cat not in categories:
                categories.append(tmp_cat)
    cursCategoryTree.close()
    cnx.close()

    return categories


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

def get_top_product_promo_info_vendor_history(pool1, pool2, pid):
    sql = "SELECT `id`, `product_id`, `vendor_id`, `task_id`, `title_en`, `title_ch`, " \
          " `desc_en`, `desc_ch`, `share_title_en`, `share_title_ch`, `share_desc_en`, `share_desc_ch`, " \
          "`img_url`, `card_width`, `card_height`, `price`, `start_date`, `end_date`, `author_id`, `keywords`, " \
          "`missed_time`, `created_time`, `confirmed_time`, `confirmer_id`" \
          " FROM `top_product_promo_info_vendor_history` WHERE `product_id`={}".format(pid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    top_product_promo_info_vendor_history = []
    if cursor.rowcount != 0:
        for (id, product_id, vendor_id, task_id, title_en, title_ch,
             desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en, share_desc_ch,
             img_url, card_width, card_height, price, start_date, end_date, author_id, keywords,
             missed_time, created_time, confirmed_time, confirmer_id
             ) in cursor:
            prop = {}
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
            if created_time is not None:
                prop["createdTime"] = int(time.mktime(time.strptime(str(created_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if confirmed_time is not None:
                prop["confirmedTime"] = int(time.mktime(time.strptime(str(confirmed_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if confirmer_id is not None:
                prop["confirmerId"] = confirmer_id

            top_product_promo_info_vendor_history.append(prop)

    cursor.close()
    cnx.close()
    return top_product_promo_info_vendor_history


def get_top_product_promo_info(pool1, pool2, pid):
    sql = "SELECT `product_id`, `title_en`, `title_ch`, " \
          " `desc_en`, `desc_ch`, `share_title_en`, `share_title_ch`, `share_desc_en`, `share_desc_ch`, " \
          "`img_url`, `card_width`, `card_height`, `deleted_time`, `created_time`, `confirmed`, `confirmed_time`" \
          " FROM `top_product_promo_info` WHERE `product_id`={}".format(pid)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    prop = {}

    if cursor.rowcount != 0:
        for (product_id, title_en, title_ch, desc_en, desc_ch, share_title_en,
             share_title_ch, share_desc_en, share_desc_ch, img_url, card_width, card_height, deleted_time,
             created_time, confirmed, confirmed_time
             ) in cursor:
            if product_id is not None:
                prop["id"] = product_id
            if title_en is not None and title_en.strip() != '':
                prop["titleEn"] = title_en
            if title_ch is not None and title_ch.strip() != '':
                prop["titleCh"] = title_ch
            if desc_en is not None and desc_en.strip() != '':
                tmp = html_parser.unescape(desc_en)
                # if not tmp.startswith('['):
                #     prop["descEn"] = [html_parser.unescape(desc_en)]
                # else:
                #     prop["descEn"] = tmp[1:-1].replace('"', '').split(',')
                prop["descEn"] = tmp
            if desc_ch is not None and desc_ch.strip() != '':
                tmp = html_parser.unescape(desc_ch)
                # if not tmp.startswith('['):
                #     prop["descCh"] = [html_parser.unescape(desc_ch)]
                # else:
                #     prop["descCh"] = tmp[1:-1].replace('"', '').split(',')
                prop["descCh"] = tmp
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
            if deleted_time is not None:
                prop["deletedTime"] = int(time.mktime(time.strptime(str(deleted_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if created_time is not None:
                prop["createdTime"] = int(time.mktime(time.strptime(str(created_time), '%Y-%m-%d %H:%M:%S')) * 1000)
            if confirmed is not None:
                prop["confirmed"] = confirmed
            if confirmed_time is not None:
                prop["confirmedTime"] = int(time.mktime(time.strptime(str(confirmed_time), '%Y-%m-%d %H:%M:%S')) * 1000)

    cursor.close()
    cnx.close()
    return prop


def get_all_data_from_product(productUnit, es, esIndex, docType, attrsType, pool1, pool2):
    """

    :param pool:
    :param productUnit:
    :param ua:
    :param es:
    :param esIndex:
    :param docType:
    :return: None
    """
    total = 0
    start = 1
    end = productUnit
    num_of_products = get_all_product_number(pool1)
    while total < num_of_products:
        # queryProduct = "SELECT `product_id`, `category_type_id`, `product_title`, `product_image_link`, " \
        #                "`product_detail`, `product_description`, `product_price`, `product_sale`, " \
        #                "`last_checked_time`, `brand_id`, `source_id`, `width`, `height`," \
        #                "`more_pictures`, `has_smart_price`, `availability`, `onSale`, `coupon_price`, `product_keywords`, `history_low_price`, `confirmed_msrp` " \
        #                "FROM `product` WHERE `product_id` BETWEEN {} AND {} and `deleted`=0".format(start, end)

        queryProduct = "SELECT `product_id`, `category_type_id`, `product_title`, `product_image_link`, " \
                       "`product_detail`, `product_description`, `product_price`, `product_sale`, " \
                       "`last_checked_time`, `brand_id`, `source_id`, `width`, `height`," \
                       "`more_pictures`, `has_smart_price`, `availability`, `onSale`, `coupon_price`, `product_keywords`, `history_low_price`, `confirmed_msrp` " \
                       "FROM `product` WHERE `product_id`={} ".format(10555664)
        cnx = pool1.connection()
        cursor = cnx.cursor()
        cursor.execute(queryProduct)
        attrs = []
        logging.info("products this time get is " + str(cursor.rowcount))
        if cursor.rowcount != 0:
            all_doc = ""
            for (product_id, category_type_id, product_title, product_image_link, product_detail,
                 product_description, product_price, product_sale, last_checked_time, brand_id, source_id, width,
                 height, more_pictures,
                 has_smart_price, availability, onSale, coupon_price, product_keywords, history_low_price,
                 confirmed_msrp
                 ) in cursor:

                total = total + 1
                logging.info("total = " + str(total))
                props = {}

                if last_checked_time is not None:
                    props["lastCheckedTime"] = int(
                        time.mktime(time.strptime(str(last_checked_time), '%Y-%m-%d %H:%M:%S')) * 1000)

                original_date = du_parser.parse(str(datetime.datetime.now()))
                props["updateESTime"] = int(time.mktime(
                    time.strptime(original_date.strftime('%Y-%m-%d %H:%M:%S.%f'), '%Y-%m-%d %H:%M:%S.%f')) * 1000)
                if history_low_price is not None and history_low_price.strip() != '' and product_price != 'N/A':
                    if '-' in history_low_price:
                        history_low_price = history_low_price.replace(' ', '')
                        pc = history_low_price.split('-')
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

                        props["currency"] = history_low_price[0]
                        props["historyLowPrice"] = {"min": min, "max": max}
                        props["historyLow"] = history_low_price
                    elif '~' in history_low_price:
                        history_low_price = history_low_price.replace(' ', '')
                        pc = history_low_price.split('~')
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
                        props["currency"] = history_low_price[0]
                        props["historyLowPrice"] = {"min": min, "max": max}
                        props["historyLow"] = history_low_price
                    else:
                        min = None
                        try:
                            min = float(get_only_numbers(history_low_price[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        max = None
                        try:
                            max = float(get_only_numbers(history_low_price[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        props["currency"] = history_low_price[0]
                        props["historyLowPrice"] = {"min": min, "max": max}
                        props["historyLow"] = history_low_price
                if confirmed_msrp is not None:
                    props["confirmedMsrp"] = confirmed_msrp
                if source_id is not None and source_id != "":
                    vendorInfo = get_vendor(pool=pool1, vendor_id=source_id)
                    if vendorInfo is not None:
                        props["language"] = vendorInfo[1]

                    vinfo = get_all_vendors(pool2, product_id, es, esIndex, attrsType)
                    if vinfo is not None:
                        sid = vinfo[0]
                        vname = vinfo[1]
                        attrs = vinfo[2]
                    if vendorInfo is not None:
                        if vendorInfo[0] not in vname:
                            vname.append(vendorInfo[0])
                        if source_id not in sid:
                            sid.append(source_id)

                    props["sourceId"] = sid
                    props["vendors"] = vname

                productPriceMax = 0
                productPriceMin = 0
                productSaleMax = 0
                productSaleMin = 0
                couponPriceMax = 0
                couponPriceMin = 0
                brands = ''
                if product_id is not None and product_id >= 0:
                    logging.info(product_id)
                    props["productId"] = product_id
                if category_type_id is not None and category_type_id >= 0:
                    props["categories"] = get_category_info_from_category_tree(pool1, category_type_id)
                    props["categoryTypeId"] = category_type_id
                if brand_id is not None and brand_id != "":
                    brands = get_brand(pool=pool1, brand_id=brand_id)
                    if len(brands) > 0:
                        props["brand"] = brands
                if product_title is not None and product_title != "":
                    if len(product_title) > 0:
                        if brands not in product_title:
                            product_title = brands + " " + product_title
                    props["productTitle"] = product_title
                if product_image_link is not None and product_image_link != "":
                    props["productImageLink"] = product_image_link
                if product_detail is not None and product_detail != "":
                    tmp = html_parser.unescape(product_detail)
                    if not tmp.startswith('['):
                        props["productDetail"] = [html_parser.unescape(product_detail)]
                    else:
                        props["productDetail"] = tmp[1:-1].replace('"', '').split(',')
                if product_description is not None and product_description != "":
                    tmp = html_parser.unescape(product_description)
                    if not tmp.startswith('['):
                        props["productDescription"] = [html_parser.unescape(product_description)]
                    else:
                        props["productDescription"] = tmp[1:-1].replace('"', '').split(',')
                if width is not None and width > 0:
                    props["width"] = width
                if height is not None and height > 0:
                    props["height"] = height
                if availability is not None:
                    if availability == 0:
                        props["availability"] = "in_stock"
                    elif availability == 1:
                        props["availability"] = "discontinued"
                    elif availability == 2:
                        props["availability"] = "out_of_stock"
                    else:
                        props["availability"] = "pre_order"

                if onSale is not None:
                    props["onSale"] = str(onSale)
                if product_keywords is not None and product_keywords.strip() != '':
                    props["keywords"] = product_keywords

                if coupon_price is not None and coupon_price != "" and product_price != 'N/A':
                    if '-' in coupon_price:
                        coupon_price = coupon_price.replace(' ', '')
                        pc = coupon_price.split('-')
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

                        props["currency"] = product_price[0]
                        props["coupon"] = {"min": min, "max": max}
                        couponPriceMin = min
                        couponPriceMax = max
                        props["couponPrice"] = coupon_price
                    elif '~' in coupon_price:
                        coupon_price = coupon_price.replace(' ', '')
                        pc = coupon_price.split('~')
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
                        props["currency"] = product_price[0]
                        props["coupon"] = {"min": min, "max": max}
                        couponPriceMin = min
                        couponPriceMax = max
                        props["couponPrice"] = coupon_price
                    else:
                        min = None
                        try:
                            min = float(get_only_numbers(coupon_price[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        max = None
                        try:
                            max = float(get_only_numbers(coupon_price[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        props["currency"] = coupon_price[0]
                        props["coupon"] = {"min": min, "max": max}
                        couponPriceMin = min
                        couponPriceMax = max
                        props["couponPrice"] = coupon_price
                if product_price is not None and product_price != "" and product_price != 'N/A':
                    if '-' in product_price:
                        product_price = product_price.replace(' ', '')
                        pc = product_price.split('-')
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
                        props["currency"] = product_price[0]
                        props["price"] = {"min": min, "max": max}
                        productPriceMax = max
                        productPriceMin = min
                        props["productPrice"] = product_price
                    elif '~' in product_price:
                        product_price = product_price.replace(' ', '')
                        pc = product_price.split('~')
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
                        props["currency"] = product_price[0]
                        props["price"] = {"min": min, "max": max}
                        productPriceMax = max
                        productPriceMin = min
                        props["productPrice"] = product_price
                    else:
                        min = None
                        try:
                            min = float(get_only_numbers(product_price[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        max = None
                        try:
                            max = float(get_only_numbers(product_price[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        props["currency"] = product_price[0]
                        props["price"] = {"min": min, "max": max}
                        productPriceMax = max
                        productPriceMin = min
                        props["productPrice"] = product_price
                if product_sale is not None and product_sale != "" and product_sale != 'N/A':
                    if '-' in product_sale:
                        product_sale = product_sale.replace(' ', '')
                        ps = product_sale.split('-')
                        min = None
                        try:
                            min = float(get_only_numbers(ps[0].strip()[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        max = None
                        try:
                            max = float(get_only_numbers(ps[1].strip()[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        props["currency"] = product_sale[0]
                        props["sale"] = {"min": min, "max": max}
                        productSaleMax = max
                        productSaleMin = min
                        props["productSale"] = product_sale
                    elif '~' in product_sale:
                        product_sale = product_sale.replace(' ', '')
                        ps = product_sale.split('~')
                        min = None
                        try:
                            min = float(get_only_numbers(ps[0].strip()[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        max = None
                        try:
                            max = float(get_only_numbers(ps[1].strip()[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        props["currency"] = product_sale[0]
                        props["sale"] = {"min": min, "max": max}
                        productSaleMax = max
                        productSaleMin = min
                        props["productSale"] = product_sale
                    else:
                        min = None
                        try:
                            min = float(get_only_numbers(product_sale.strip()[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        max = None
                        try:
                            max = float(get_only_numbers(product_sale.strip()[1:]))
                        except ValueError, e:
                            logging.error('ProductId=' + str(product_id))
                            logging.error(e)
                            continue
                        props["currency"] = product_sale[0]
                        props["sale"] = {"min": min, "max": max}
                        productSaleMax = max
                        productSaleMin = min
                        props["productSale"] = product_sale
                if productPriceMax == productPriceMin:
                    # productPrice.max == productPrice.min
                    if productSaleMax == productSaleMin:
                        # productSale.max == productSale.min
                        if productPriceMax != 0.00:
                            # productPrice.max != 0.00
                            tmp = (1 - productSaleMax / productPriceMax) * 100
                            discountStr = {}
                            discountStr["min"] = tmp
                            discountStr["max"] = tmp
                            discountStr["discountStr"] = str(tmp) + "%"
                            props["discount"] = discountStr
                        else:
                            discountStr = {}
                            discountStr["min"] = 0.00
                            discountStr["max"] = 0.00
                            discountStr["discountStr"] = str(0.00) + "%"
                            props["discount"] = discountStr
                    else:
                        if productPriceMax != 0.00:
                            # productPrice.max != 0
                            tmpMin = (1 - productSaleMax / productPriceMax) * 100
                            tmpMax = (1 - productSaleMin / productPriceMax) * 100
                            discountStr = {}
                            discountStr["min"] = tmpMin
                            discountStr["max"] = tmpMax
                            discountStr["discountStr"] = str(tmpMin) + "%-" + str(tmpMax) + "%"
                            props["discount"] = discountStr
                        else:
                            # productPrice.max = 0
                            discountStr = {}
                            discountStr["min"] = 0.00
                            discountStr["max"] = 0.00
                            discountStr["discountStr"] = str(0.00) + "%"
                            props["discount"] = discountStr
                # else:
                #     # productPrice.max != productPrice.min
                #     if props["productSale"]["max"] == props["productSale"]["min"]:
                #         # productSale.max == productSale.min
                #         if props["productPrice"]["max"] != 0.00 and props["productPrice"]["min"] != 0.00:
                #             # productPrice.max != 0.00 and productPrice.min != 0.00
                #             tmpMin = (1 - props["productSale"]["max"] / props["productPrice"]["max"]) * 100
                #             tmpMax = (1 - props["productSale"]["max"] / props["productPrice"]["min"]) * 100
                #             discountStr = {}
                #             discountStr["min"] = tmpMin
                #             discountStr["max"] = tmpMax
                #             discountStr["discountStr"] = str(tmpMin) + "%-" + str(tmpMax) + "%"
                #             props["discountStr"] = discountStr
                #         elif props["productPrice"]["max"] != 0.00:
                #             tmpMin = (1 - props["productSale"]["max"] / props["productPrice"]["max"]) * 100
                #             discountStr = {}
                #             discountStr["min"] = tmpMin
                #             discountStr["max"] = None
                #             discountStr["discountStr"] = str(tmpMin) + "%"
                #             props["discountStr"] = discountStr
                #             # productPrice.max == 0.00 or productPrice.min == 0
                #     else:
                #         # productSale.max != productSale.min
                #         if props["productPrice"]["max"] != 0.00 and props["productPrice"]["min"] != 0.00:
                #             tmpMax = (1 - props["productSale"]["max"] / props["productPrice"]["min"]) * 100
                #             tmpMin = (1 - props["productSale"]["min"] / props["productPrice"]["max"]) * 100
                #             discountStr = {}
                #             discountStr["min"] = tmpMin
                #             discountStr["max"] = tmpMax
                #             discountStr["discountStr"] = str(tmpMin) + "%-" + str(tmpMax) + "%"
                #             props["discountStr"] = discountStr
                #         elif props["productPrice"]["max"] != 0.00:
                #             tmpMin = (1 - props["productSale"]["min"] / props["productPrice"]["max"]) * 100
                #             discountStr = {}
                #             discountStr["min"] = tmpMin
                #             discountStr["max"] = None
                #             discountStr["discountStr"] = str(tmpMin) + "%"
                #             props["discountStr"] = discountStr
                # pp = float(product_price[1:])
                # ps = float(product_sale[1:])
                # if pp != 0.00:
                #     discountStr = (1 - float(product_sale[1:]) / float(product_price[1:])) * 100
                #     props["discountStr"] = str(discountStr) + '%'
                #     props["discountMetric"] = discountStr
                # else:
                #     discountStr = 0.0
                #     props["discountStr"] = str(discountStr) + '%'
                #     props["discountMetric"] = discountStr

                if more_pictures is not None:
                    props["morePictures"] = more_pictures
                if has_smart_price is not None:
                    props["hasSmartPrice"] = has_smart_price
                props["channel"] = str(1)
                props["attribute"] = attrs
                top_product_promo_info_vendor = get_top_product_promo_info_vendor(pool1, pool2, product_id)
                if top_product_promo_info_vendor is not None and len(top_product_promo_info_vendor) != 0:
                    props["topProductPromoInfoVendor"] = top_product_promo_info_vendor
                    props["topProduct"] = True
                    props["promo"] = ["promo_v"]
                top_product_promo_info = get_top_product_promo_info(pool1, pool2, product_id)
                if top_product_promo_info is not None and len(top_product_promo_info) != 0:
                    props["topProductPromoInfo"] = top_product_promo_info
                top_product_promo_info_vendor_history = get_top_product_promo_info_vendor_history(pool1, pool2, product_id)
                if top_product_promo_info_vendor_history is not None and len(top_product_promo_info_vendor_history) != 0:
                    props["topProductPromoInfoVendorHistory"] = top_product_promo_info_vendor_history
                upsert = {"doc": props, 'doc_as_upsert': True}
                action = make_action(id=product_id, vendor_id=source_id)
                doc = json.dumps(upsert, use_decimal=True)
                all_doc += action + "\n" + doc + "\n"

            if all_doc.strip() != '':
                try:
                    es.bulk(index=esIndex, doc_type=docType, body=all_doc)
                except UnicodeDecodeError, e:
                    logging.error(product_id)
                    logging.error(e)
                    pass
                except ElasticsearchException, e:
                    logging.error(product_id)
                    logging.error(e)

        else:
            cnx.close()

        cursor.close()
        cnx.close()
        start = end + 1
        end = end + productUnit
        break


def make_query_body_for_brand(brand):
    query_body = {
        "size": 10,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": "en",
                        "fields": ["language"]
                    }
                },
                "must": {
                    "multi_match": {
                        "query": brand,
                        "fields": ["brand"]
                    }
                }
            }
        }
    }

    return query_body


def make_query_body_for_categories(categories):
    query_body = {
        "size": 10,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": "en",
                        "fields": ["language"]
                    }
                },
                "must": {
                    "multi_match": {
                        "query": categories,
                        "fields": ["categories"]
                    }
                }
            }
        }
    }

    return query_body


def make_query_body_for_vendors(vendors):
    query_body = {
        "size": 10,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": "en",
                        "fields": ["language"]
                    }
                },
                "must": {
                    "multi_match": {
                        "query": vendors,
                        "fields": ["vendors"]
                    }
                }
            }
        }
    }

    return query_body


def sanity_check_with_error_handler(itemlist, idx, docType, query_body_maker, count_for_sanity_check):
    for itm in itemlist:
        try:
            res = es.search(index=idx, doc_type=docType, body=query_body_maker(itm))
            if res is not None and 'hits' in res.keys():
                count_for_sanity_check = count_for_sanity_check + len(res['hits'])
        except TransportError, e:
            logging.error(str(e))

    return count_for_sanity_check


def index_exists(es_client, index_name):
    try:
        return es_client.indices.exists(index_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def index_delete(es_client, index_name):
    try:
        return es_client.indices.delete(index_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def index_create(es_client, index_name):
    try:
        return es_client.indices.create(index_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def alias_exists(es_client, alias_name):
    try:
        return es_client.indices.exists_alias(name=args.esIndex)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def alias_get(es_client, alias_name):
    try:
        return es_client.indices.get_alias(name=args.esIndex)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def alias_put(es_client, alias_name, index_name):
    try:
        return es_client.indices.put_alias(index_name, alias_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_product2_pro.log', level=logging.DEBUG,
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
    parser.add_argument('--esIndex', default='search')
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
    res = {}
    if alias_exists(es, args.esIndex):
        res = alias_get(es, args.esIndex)

    name_a = 'search_a'
    name_b = 'search_b'

    keys = res.keys()
    flag = False
    if len(keys) == 0:
        new_es_name = name_a
        old_es_name = name_b
        logging.info("Create index(new) " + new_es_name)
        if index_exists(es, new_es_name):
            index_delete(es, new_es_name)
        index_create(es, new_es_name)
        logging.info("Put alias " + args.esIndex)
        flag = True
    else:
        old_es_name = None
        keys = res.keys()
        if keys is not None and len(keys) > 0:
            old_es_name = keys[0]

        if old_es_name == name_a:
            new_es_name = name_b
        else:
            new_es_name = name_a

        logging.debug("Start Importing")
        if not index_exists(es, new_es_name):
            logging.info("Create index(new) " + new_es_name)
            index_create(es, new_es_name)
        else:
            logging.info("Delete index(new), and recreate it")
            index_delete(es, new_es_name)
            index_create(es, new_es_name)

    get_all_data_from_product(int(args.productUnit), es, new_es_name, args.docType, args.attrsType, pool1, pool2)

    # count = 0
    # try:
    #     count = es.cat.count(index=new_es_name)
    # except TransportError, e:
    #     logging.error(str(e))
    # logging.info(count)
    #
    # count_for_sanity_check = 0
    # popular_brands = ["Nike", "Michael Kors", "La Mer", "adidas", "Bose", "Dyson", "Kate Spade", "Pandora",
    #                   "Timberland"]
    # popular_categories = ["toys", "beauty", "bags", "sport & outdoors", "apparel", "baby gear & essentials", "shoes",
    #                       "jewelry & accessories", "home", "health & food", "movies & tv"]
    # popular_vendors = ["6pm", "Bloomingdales", "Macy's", "Nordstrom", "Saks Fifth Avenue", "Stride Rite", "Amazon",
    #                    "Kohl's", "Neiman Marcus Last Call", "Ralph Lauren", "Saks Off 5th", "Walmart"]
    #
    # count_for_sanity_check = sanity_check_with_error_handler(popular_brands, new_es_name, args.docType,
    #                                                          make_query_body_for_brand, count_for_sanity_check)
    # count_for_sanity_check = sanity_check_with_error_handler(popular_categories, new_es_name, args.docType,
    #                                                          make_query_body_for_categories, count_for_sanity_check)
    # count_for_sanity_check = sanity_check_with_error_handler(popular_vendors, new_es_name, args.docType,
    #                                                          make_query_body_for_vendors, count_for_sanity_check)
    #
    # data_check_total = len(popular_brands) * 30 + len(popular_categories) * 30 + len(popular_vendors) * 30
    # logging.info(count_for_sanity_check)
    #
    # if count >= 3000000L:  # and count_for_sanity_check >= data_check_total:
    #     logging.info("Put Alias " + new_es_name)
    #     alias_put(es, args.esIndex, new_es_name)
    #     if not flag:
    #         if old_es_name is not None:
    #             if index_exists(es, old_es_name):
    #                 logging.info("Delete index(old) " + old_es_name)
    #                 index_delete(es, old_es_name)
    # else:
    #     if not flag:
    #         logging.info("Do NOT satisfy the requirements for data sanity, delete the newly created index")
    #         index_delete(es, new_es_name)
    #     else:
    #         alias_put(es, args.esIndex, new_es_name)

    # if count > 1000:
    #     logging.info("Put Alias " + new_es_name)
    #     alias_put(es, args.esIndex, new_es_name)
    #     if not flag:
    #         if old_es_name is not None:
    #             if index_exists(es, old_es_name):
    #                 logging.info("Delete index(old) " + old_es_name)
    #                 index_delete(es, old_es_name)
    # else:
    #     index_delete(es, new_es_name)

    alias_put(es, args.esIndex, new_es_name)
    if old_es_name is not None:
        if index_exists(es, old_es_name):
            logging.info("Delete index(old) " + old_es_name)
            index_delete(es, old_es_name)

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
    pool1.close()
    pool2.close()