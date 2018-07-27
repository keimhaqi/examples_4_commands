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
import simplejson as json
import time
from decimal import Decimal
import hashlib
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')

html_parser = HTMLParser.HTMLParser()
hash = hashlib.sha1()

vendors = {}


def make_action(id):
    action = {"update": {"_id": str(id)}}
    return json.dumps(action)


def get_all_link_number(pool):
    """

    :param pool:
    :return: number
    """
    query_product_number = "SELECT count(`ID`) FROM `link`"
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


def get_vendor_info(pool1, vendor_id):
    sql = "SELECT `vendor_name_en` FROM `vendor` WHERE `vendor_id`={}".format(vendor_id)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    vendor_name = None
    for vendor_name_en in cursor:
        vendor_name = vendor_name_en

    cursor.close()
    cnx.close()
    return vendor_name


def vendor_handler(pool, product_id, vendor_id):
    vendors = []
    pids = []
    if vendor_id == 6 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_6pm')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 3 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_amazon')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 5 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_amazon_cn')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 13867 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_bloomingdales')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 3184 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_macys')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 1237 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_nordstrom')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 2 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_ralphlauren')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 13816 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_saks')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 38801 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_saksoff')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 38655 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_striderite')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 36025 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_lastcall')
        if pid is not None:
            pids.append(pid)
    if vendor_id == 2149 and product_id is not None:
        pid = get_all_vendors(pool, product_id, 'product_sku_walmart')
        if pid is not None:
            pids.append(pid)

    return pids


def get_all_vendors(pool, pid, table_name):
    query_vendor = "SELECT `product_id` FROM `{}` WHERE `id`={}".format(table_name, pid)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_vendor)
    ret = None
    if cursor.rowcount != 0:
        for (product_id) in cursor:
            ret = product_id[0]

    cursor.close()
    cnx.close()
    return ret


def get_info_from_t_crawl_url(pool1, pool2, url_ids):
    sql = 'SELECT `id`, `jinbag_id`, `domain_id` FROM `t_crawl_url` WHERE `id` IN ({})'.format(','.join(url_ids))
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    jinbag_id_domain_id = []
    if cursor.rowcount != 0:
        for (id, jinbag_id, domain_id) in cursor:
            rets = vendor_handler(pool2, jinbag_id, domain_id)
            if rets is not None and len(rets) > 0:
                for it in rets:
                    if it not in jinbag_id_domain_id:
                        jinbag_id_domain_id.append({"jinbagId": it, "domain_id": str(domain_id)})

    cursor.close()
    cnx.close()
    return jinbag_id_domain_id


def get_data_from_seed_url(pool1, pool2, url_id):
    ret = []
    query = 'SELECT `seed_id`, `url_id`, `status` FROM  `seed_url` WHERE `seed_id`={}'.format(url_id)
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    seeds = []
    for (seed_id, url_id, status) in cursor:
        seeds.append(str(url_id))

    cursor.close()
    cnx.close()
    return seeds


def price_handler(price):
    props = {}
    if '-' in price:
        price = price.replace(' ', '')
        pc = price.split('-')
        min = 0
        try:
            min = float(get_only_numbers(pc[0].strip()[1:]))
        except ValueError, ve:
            logging.error(ve)
        max = 0
        try:
            max = float(get_only_numbers(pc[1].strip()[1:]))
        except ValueError, ve:
            logging.error(ve)
        props["min"] = min
        props["max"] = max
    elif '~' in price:
        price = price.replace(' ', '')
        pc = price.split('~')
        min = 0
        try:
            min = float(get_only_numbers(pc[0].strip()[1:]))
        except ValueError, ve:
            logging.error(ve)
        max = 0
        try:
            max = float(get_only_numbers(pc[1].strip()[1:]))
        except ValueError, ve:
            logging.error(ve)
        props["min"] = min
        props["max"] = max
    else:
        min = 0
        try:
            min = float(get_only_numbers(price[1:]))
        except ValueError, ve:
            logging.error(ve)
        max = 0
        try:
            max = float(get_only_numbers(price[1:]))
        except ValueError, ve:
            logging.error(ve)
        props["min"] = min
        props["max"] = max
    return props


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


def get_price_with_category_from_product(pool1, pool2, product_id):
    sql = "SELECT `product_price`, `product_sale`, `category_type_id`, `brand_id` FROM `product` WHERE `product_id`={}".format(
        product_id)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    props = {}
    productPriceMax = 0
    productPriceMin = 0
    productSaleMax = 0
    productSaleMin = 0
    if cursor.rowcount != 0:
        for (product_price, product_sale, category_type_id, brand_id) in cursor:
            if product_price is not None:
                tmp_price = price_handler(product_price)

                productPriceMin = tmp_price["min"]
                productPriceMax = tmp_price["max"]
            if product_sale is not None:
                tmp_sale = price_handler(product_sale)

                props["min"] = tmp_price["min"]
                props["max"] = tmp_price["max"]
                productSaleMin = tmp_sale["min"]
                productSaleMax = tmp_sale["max"]
            if category_type_id is not None:
                props["category"] = get_category_info_from_category_tree(pool1, category_type_id)
            if brand_id is not None:
                brand = get_brand(pool1, brand_id)
                if brand != '':
                    props["brand"] = brand

    if productPriceMax == productPriceMin:
        # productPrice.max == productPrice.min
        if productSaleMax == productSaleMin:
            # productSale.max == productSale.min
            if productPriceMax != 0.00:
                # productPrice.max != 0.00
                tmp = (1 - productSaleMax / productPriceMax) * 100
                props["discount_min"] = tmp
                props["discount_max"] = tmp
            else:
                props["discount_min"] = 0.00
                props["discount_max"] = 0.00
        else:
            if productPriceMax != 0.00:
                # productPrice.max != 0
                tmpMin = (1 - productSaleMax / productPriceMax) * 100
                tmpMax = (1 - productSaleMin / productPriceMax) * 100
                props["discount_min"] = tmpMin
                props["discount_max"] = tmpMax
            else:
                props["discount_min"] = 0.00
                props["discount_max"] = 0.00

    return props


def get_brand_and_category_from_level_three(pool1, pool2, jinbagId, domain_id):
    ret = {}
    brands = []
    category = []

    if jinbagId is not None and domain_id in vendors.keys():
        vend = vendors.get(domain_id)
        sql = 'SELECT `brand`, `product_id` FROM `{}` WHERE `id`={}'.format(vend[1], jinbagId)
        cnx = pool2.connection()
        cursor = cnx.cursor()
        cursor.execute(sql)

        if cursor.rowcount != 0:
            for (brand, product_id) in cursor:
                tmp = get_price_with_category_from_product(pool1, pool2, jinbagId)
                keys = tmp.keys()
                if "discount_min" in keys:
                    ret["discount_min"] = tmp["discount_min"]
                if "discount_max" in keys:
                    ret["discount_max"] = tmp["discount_max"]
                if "min" in keys:
                    ret["min"] = tmp["min"]
                if "max" in keys:
                    ret["max"] = tmp["max"]
                if "category" in keys:
                    category = category + tmp["category"]
                if "brand" in keys:
                    for b in tmp["brand"]:
                        if b not in brands:
                            brands.append(b)

        cursor.close()
        cnx.close()
    ret["brand"] = brands
    ret["category"] = category
    return ret


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


def get_whole_product2_info(pool1, pool2, jinbag_id):
    if jinbag_id is None:
        return {}
    sql = 'SELECT `brand_id`, `category_type_id`, `product_price`, `product_sale` FROM `product` WHERE `product_id`={}'.format(
        jinbag_id)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    ret = {}
    if cursor.rowcount != 0:
        for (brand_id, category_type_id, product_price, product_sale) in cursor:
            if brand_id is not None and brand_id > 0:
                brand = get_brand(pool1, brand_id)
                if brand.strip() != '':
                    ret["brand"] = brand
            if category_type_id is not None and category_type_id > 0:
                category = get_category_info_from_category_tree(pool1, category_type_id)
                if len(category) != 0:
                    ret["category"] = category
            if product_price is not None:
                tmp_price = price_handler(product_price)
                productPriceMin = tmp_price["min"]
                productPriceMax = tmp_price["max"]
            if product_sale is not None:
                tmp_sale = price_handler(product_sale)
                ret["min"] = tmp_price["min"]
                ret["max"] = tmp_price["max"]
                productSaleMin = tmp_sale["min"]
                productSaleMax = tmp_sale["max"]
        if productPriceMax == productPriceMin:
            # productPrice.max == productPrice.min
            if productSaleMax == productSaleMin:
                # productSale.max == productSale.min
                if productPriceMax != 0.00:
                    # productPrice.max != 0.00
                    tmp = (1 - productSaleMax / productPriceMax) * 100
                    ret["discount_min"] = tmp
                    ret["discount_max"] = tmp
                else:
                    ret["discount_min"] = 0.00
                    ret["discount_max"] = 0.00
            else:
                if productPriceMax != 0.00:
                    # productPrice.max != 0
                    tmpMin = (1 - productSaleMax / productPriceMax) * 100
                    tmpMax = (1 - productSaleMin / productPriceMax) * 100
                    ret["discount_min"] = tmpMin
                    ret["discount_max"] = tmpMax
                else:
                    ret["discount_min"] = 0.00
                    ret["discount_max"] = 0.00

    cursor.close()
    cnx.close()

    return ret


def import_link(pool1, pool2, es, esIndex, docType, productUnit):
    total = 0
    start = 0
    end = productUnit
    num_of_link = get_all_link_number(pool1)
    while total < num_of_link:
        sql = "SELECT `ID`, `visible`, `display_type`, `data_type`, `title`, `click_url`, " \
              "`end_date`, `start_date`, `end_time_confirmed`, `mid`, `nid`, `card_img`, `card_width`, " \
              "`card_height`, `coupon_img`, `coupon_width`, `coupon_height`, `banner_img`, `banner_width`, `banner_height`, `c_title`, `long_desc`, " \
              "`c_long_desc`, `short_desc`, `c_short_desc`, `price`, `task_id`, `jinbag_id`, " \
              "`sale_type`, `data_source`, `sale_restriction`, `coupon_code`, `time`, `missed_time` FROM `link` WHERE `ID` BETWEEN {} AND {} AND `data_type`=0".format(
            start, end)
        cnx = pool1.connection()
        cursor = cnx.cursor()
        cursor.execute(sql)
        all_doc = ""
        if cursor.rowcount != 0:
            for (ID, visible, display_type, data_type, title, click_url, end_date, start_date,
                 end_time_confirmed, mid, nid, card_img, card_width, card_height, coupon_img,
                 coupon_width, coupon_height, banner_img, banner_width, banner_height, c_title, long_desc, c_long_desc,
                 short_desc,
                 c_short_desc, price, task_id, jinbag_id, sale_type, data_source, sale_restriction,
                 coupon_code, ttime, missed_time) in cursor:
                props = {}
                total = total + 1
                props = {}
                if ID is not None:
                    props["id"] = str(ID)
                if ID == 4108:
                    print(ID)
                if visible is not None:
                    props["visible"] = str(visible)
                if data_type is not None:
                    props["dataType"] = data_type
                    if task_id is not None:
                        brand = []
                        category = []
                        vend = []
                        pids = []
                        if data_type == 0:
                            url_ids = get_data_from_seed_url(pool1, pool2, task_id)
                            if len(url_ids) != 0:
                                jinbagId = get_info_from_t_crawl_url(pool1, pool2, url_ids)
                                max = 0
                                min = 100000000.0
                                discount = {}
                                for iter in jinbagId:
                                    if iter["domain_id"] in vendors.keys():
                                        v_name = vendors.get(iter["domain_id"])[1]
                                        if v_name not in vend:
                                            vend.append(v_name)
                                    b_c = get_brand_and_category_from_level_three(pool1, pool2, iter["jinbagId"],
                                                                                  iter["domain_id"])
                                    keys = b_c.keys()
                                    if "brand" in keys:
                                        for it in b_c["brand"]:
                                            if it not in brand:
                                                brand.append(it)
                                    if "discount_min" in keys:
                                        discount["min"] = b_c["discount_min"]
                                    if "discount_max" in keys:
                                        discount["max"] = b_c["discount_max"]
                                    if "min" in keys:
                                        if min >= b_c["min"]:
                                            min = b_c["min"]
                                    if "max" in keys:
                                        if max <= b_c["max"]:
                                            max = b_c["max"]
                                    if "category" in keys:
                                        props["categories"] = b_c["category"]
                                    if iter["jinbagId"] is not None:
                                        pids.append(str(iter["jinbagId"]))
                                sale = {}
                                sale["min"] = min
                                sale["max"] = max
                                props["linkSale"] = sale
                                props["products"] = pids
                                props["discount"] = discount
                        # elif data_type == 1:
                        #     min = 100000000.0
                        #     max = 0
                        #     product_info = get_whole_product2_info(pool1, pool2, jinbag_id)
                        #     keys = product_info.keys()
                        #     if "brand" in keys:
                        #         brand.append(product_info["brand"])
                        #     discountStr = {}
                        #     if "discount_min" in keys:
                        #         discountStr["min"] = product_info["discount_min"]
                        #     if "discount_max" in keys:
                        #         discountStr["max"] = product_info["discount_max"]
                        #     props["discount"] = discountStr

                        #     if "min" in keys:
                        #         if min >= product_info["min"]:
                        #             min = product_info["min"]
                        #     if "max" in keys:
                        #         if max <= product_info["max"]:
                        #             max = product_info["max"]
                        #     if "category" in keys:
                        #         props["categories"] = product_info["category"]
                        #     pids.append(jinbag_id)
                        #     sale = {}
                        #     sale["min"] = min
                        #     sale["max"] = max
                        #     props["linkSale"] = sale
                        #     props["products"] = pids
                        if len(brand) != 0:
                            props["brand"] = brand

                        if len(category) != 0:
                            props["categories"] = category
                if title is not None:
                    props["title"] = title
                if end_date is not None:
                    props["endDate"] = int(time.mktime(time.strptime(str(end_date), '%Y-%m-%d %H:%M:%S')) * 1000)
                if start_date is not None:
                    props["startDate"] = int(time.mktime(time.strptime(str(start_date), '%Y-%m-%d %H:%M:%S')) * 1000)
                if mid is not None:
                    vendor_name = get_vendor_info(pool1, mid)
                    if vendor_name is not None:
                        props["vendors"] = vendor_name
                if card_img is not None:
                    props["cardImg"] = card_img
                if card_width is not None:
                    props["cardWidth"] = card_width
                if card_height is not None:
                    props["cardHeight"] = card_height
                if c_title is not None:
                    props["cTitle"] = c_title
                if long_desc is not None:
                    props["longDesc"] = long_desc
                if c_long_desc is not None:
                    props["cLongDesc"] = c_long_desc
                if short_desc is not None:
                    props["shortDesc"] = short_desc
                if c_short_desc is not None:
                    props["cShortDesc"] = c_short_desc
                upsert = {"doc": props, 'doc_as_upsert': True}
                action = make_action(id=ID)
                doc = json.dumps(upsert, use_decimal=True)
                all_doc += action + "\n" + doc + "\n"

            if all_doc.strip() != '':
                try:
                    es.bulk(index=esIndex, doc_type=docType, body=all_doc)
                except UnicodeDecodeError, e:
                    logging.error(e)
        else:
            cnx.close()

        cursor.close()
        cnx.close()
        start = end + 1
        end = end + productUnit


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_link_pro.log', level=logging.DEBUG,
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

    parser.add_argument('--productUnit', default='1000')
    parser.add_argument('--esIndex', default='search')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--docType', default='link')

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

    index_mappings = {

        "properties": {
            "id": {
                "type": "long"
            },
            "visible": {
                "type": "long"
            },
            "displayType": {
                "type": "long"
            },
            "dataType": {
                "type": "long"
            },
            "title": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },
                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "endDate": {
                "type": "date",
                "format": "epoch_millis"
            },
            "startDate": {
                "type": "date",
                "format": "epoch_millis"
            },
            "vendors": {
                "type": "text",
                "analyzer": "my_analyzer",
                "norms": {
                    "enabled": False
                },
                "include_in_all": True
            },
            "cardImg": {
                "type": "text"
            },
            "cardWidth": {
                "type": "long"
            },
            "cardHeight": {
                "type": "long"
            },
            "cTitle": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },
                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "longDesc": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },
                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "cLongDesc": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },
                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "shortDesc": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },

                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "cShortDesc": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },

                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "taskId": {
                "type": "long",
            },
            "brand": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },

                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "categories": {
                "type": "text",
                "term_vector": "with_positions_offsets",
                "norms": {
                    "enabled": False
                },

                "analyzer": "my_analyzer",
                "include_in_all": True
            },
            "linkSale": {
                "properties": {
                    "min": {
                        "type": "float",
                        "index": "not_analyzed"
                    },
                    "max": {
                        "type": "float",
                        "index": "not_analyzed"
                    }
                }
            },
            "discount": {
                "properties": {
                    "min": {
                        "type": "double",
                        "index": "not_analyzed"
                    },
                    "max": {
                        "type": "double",
                        "index": "not_analyzed"
                    },
                    "discountStr": {
                        "type": "text"
                    }
                }
            }
        }
    }
    es = Elasticsearch()
    es.indices.put_mapping(doc_type=args.docType, body=index_mappings, index=args.esIndex)
    logging.info("Start Importing")

    file = open("./vendor.properties")
    line = file.readline()
    while line:
        v_info = line.replace('\n', '').split(',')
        vendors[v_info[0]] = [v_info[1], v_info[2]]
        line = file.readline()

    import_link(pool1, pool2, es, args.esIndex, args.docType, int(args.productUnit))
    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
    pool1.close()
    pool2.close()