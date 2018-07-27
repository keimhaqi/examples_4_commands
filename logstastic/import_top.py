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
from decimal import Decimal
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


def make_action(id):
    action = {"update": {"_id": str(id)}}
    return json.dumps(action)


def make_parent_action(id, vendor_name, product_id):
    action = {"index": {"_id": str(vendor_name + "_" + str(id)), "parent": str(product_id)}}
    return json.dumps(action)


def get_all_top_product_promo_info_vendor_history(pool):
    """

    :param pool:
    :return: number
    """
    query_product_number = "SELECT count(`id`) FROM `top_product_promo_info_vendor_history`"
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
    tmp = {}
    if vendor_id is not None:
        query_vendor = "SELECT `vendor_id`, `vendor_logo_width`, `vendor_logo_height`, `vendor_logo_url` FROM `vendor` WHERE `vendor_id`={}".format(
            vendor_id)
        cnx = pool.connection()
        cursor = cnx.cursor()
        cursor.execute(query_vendor)
        for vendor_id, vendor_logo_width, vendor_logo_height, vendor_logo_url in cursor:
            tmp["vendor_logo_url"] = vendor_logo_url
            tmp["vendor_logo_width"] = vendor_logo_width
            tmp["vendor_logo_height"] = vendor_logo_height

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


def get_top_product_promo_info_vendor_history(pool1, es, esIndex, docType, start, end):
    sql = "SELECT `id`, `product_id`, `vendor_id`, `task_id`, `title_en`, `title_ch`, " \
          " `desc_en`, `desc_ch`, `share_title_en`, `share_title_ch`, `share_desc_en`, `share_desc_ch`, " \
          "`img_url`, `card_width`, `card_height`, `price`, `start_date`, `end_date`, `author_id`, `keywords`, " \
          "`missed_time`, `created_time`, `confirmed_time`, `confirmer_id`" \
          " FROM `top_product_promo_info_vendor_history` WHERE `id` BETWEEN {} and {} and `end_date`>='2018-3-26 23:59:59' group by `product_id`".format(
        start, end)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    if cursor.rowcount != 0:
        all_doc = ""
        product = {}
        tph = []
        # prd_id = None
        for (id, product_id, vendor_id, task_id, title_en, title_ch,
             desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en, share_desc_ch,
             img_url, card_width, card_height, price, start_date, end_date, author_id, keywords,
             missed_time, created_time, confirmed_time, confirmer_id
             ) in cursor:
            logging.info(
                "id = {}, product_id = {}, vendor_id = {}, task_id = {}, title_en = {}, title_ch = {}, desc_en = {}, desc_ch = {}, share_title_en = {}, share_title_ch = {}, share_desc_en = {}, share_desc_ch = {}"
                .format(id, product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en,
                        share_title_ch, share_desc_en, share_desc_ch) +
                ", img_url = {}, card_width = {}, card_height = {}, price = {}, start_date = {}, end_date = {}, author_id = {}, keywords = {}, missed_time = {}, created_time = {}, confirmed_time = {}, confirmer_id = {}"
                .format(img_url, card_width, card_height, price, start_date, end_date, author_id, keywords, missed_time,
                        created_time, confirmed_time, confirmer_id)
                )
            top_product_promo_info_vendor_history = {}
            if product_id is not None:
                top_product_promo_info_vendor_history["id"] = product_id
                prd_id = product_id
            if vendor_id is not None:
                top_product_promo_info_vendor_history["vendorId"] = vendor_id
                vendor_logo_url = get_vendor_logo_url(pool1, vendor_id)
                if vendor_logo_url is not None and len(vendor_logo_url) > 0 and isinstance(vendor_logo_url, dict):
                    keys = vendor_logo_url.keys()
                    if "vendor_logo_url" in keys and vendor_logo_url["vendor_logo_url"] is not None:
                        top_product_promo_info_vendor_history["vendorLogoUrl"] = vendor_logo_url["vendor_logo_url"]
                    if "vendor_logo_width" in keys and vendor_logo_url["vendor_logo_width"] is not None:
                        top_product_promo_info_vendor_history["vendorLogoWidth"] = vendor_logo_url["vendor_logo_width"]
                    if "vendor_logo_height" in keys and vendor_logo_url["vendor_logo_height"] is not None:
                        top_product_promo_info_vendor_history["vendorLogoHeight"] = vendor_logo_url[
                            "vendor_logo_height"]
            if task_id is not None:
                top_product_promo_info_vendor_history["taskId"] = task_id
            if title_en is not None and title_en.strip() != '':
                top_product_promo_info_vendor_history["titleEn"] = title_en
            if title_ch is not None and title_ch.strip() != '':
                top_product_promo_info_vendor_history["titleCh"] = title_ch
            if desc_en is not None and desc_en.strip() != '':
                tmp = html_parser.unescape(desc_en)
                top_product_promo_info_vendor_history["descEn"] = tmp
            if desc_ch is not None and desc_ch.strip() != '':
                tmp = html_parser.unescape(desc_ch)
                top_product_promo_info_vendor_history["descCh"] = tmp
            if share_title_en is not None and share_title_en.strip() != '':
                top_product_promo_info_vendor_history["shareTitleEn"] = share_title_en
            if share_title_ch is not None and share_title_ch.strip() != '':
                top_product_promo_info_vendor_history["shareTitleCh"] = share_title_ch
            if share_desc_en is not None and share_desc_en.strip() != '':
                top_product_promo_info_vendor_history["shareDescEn"] = share_desc_en
            if share_desc_ch is not None and share_desc_ch.strip() != '':
                top_product_promo_info_vendor_history["shareDescCh"] = share_desc_ch
            if img_url is not None and img_url.strip() != '':
                top_product_promo_info_vendor_history["imgUrl"] = img_url
            if card_width is not None and card_width >= 0:
                top_product_promo_info_vendor_history["cardWidth"] = card_width
            if card_height is not None and card_height >= 0:
                top_product_promo_info_vendor_history["cardHeight"] = card_height
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

                    top_product_promo_info_vendor_history["topPrice"] = {"min": min, "max": max}
                    top_product_promo_info_vendor_history["price"] = price
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
                    top_product_promo_info_vendor_history["topPrice"] = {"min": min, "max": max}
                    top_product_promo_info_vendor_history["price"] = price
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
                    top_product_promo_info_vendor_history["topPrice"] = {"min": min, "max": max}
                    top_product_promo_info_vendor_history["price"] = price
            if start_date is not None:
                try:
                    top_product_promo_info_vendor_history["startDate"] = int(
                        time.mktime(time.strptime(str(start_date), '%Y-%m-%d %H:%M:%S')) * 1000)
                except ValueError, e:
                    logging.error("start_date = " + str(start_date) + ", " + str(e))
            if end_date is not None:
                try:
                    top_product_promo_info_vendor_history["endDate"] = int(
                        time.mktime(time.strptime(str(end_date), '%Y-%m-%d %H:%M:%S')) * 1000)
                except ValueError, e:
                    logging.error("end_date = " + str(end_date) + ", " + str(e))
            if author_id is not None:
                top_product_promo_info_vendor_history["authorId"] = author_id
            if keywords is not None and keywords.strip() != '':
                top_product_promo_info_vendor_history["keywords"] = keywords
            if missed_time is not None:
                try:
                    top_product_promo_info_vendor_history["missedTime"] = int(
                        time.mktime(time.strptime(str(missed_time), '%Y-%m-%d %H:%M:%S')) * 1000)
                except ValueError, e:
                    logging.error("missed_time = " + str(missed_time) + ", " + str(e))
            if created_time is not None:
                try:
                    top_product_promo_info_vendor_history["createdTime"] = int(
                        time.mktime(time.strptime(str(created_time), '%Y-%m-%d %H:%M:%S')) * 1000)
                except ValueError, e:
                    logging.error("created_time = " + str(created_time) + ", " + str(e))
            if confirmed_time is not None:
                try:
                    top_product_promo_info_vendor_history["confirmedTime"] = int(
                        time.mktime(time.strptime(str(confirmed_time), '%Y-%m-%d %H:%M:%S')) * 1000)
                except ValueError, e:
                    logging.error("confirmed_time = " + str(confirmed_time) + ", " + str(e))
            if confirmer_id is not None:
                top_product_promo_info_vendor_history["confirmerId"] = confirmer_id

            tph.append(top_product_promo_info_vendor_history)

        product["productId"] = product_id
        original_date = du_parser.parse(str(datetime.datetime.now()))
        try:
            product["updateESTime"] = int(time.mktime(
                time.strptime(original_date.strftime('%Y-%m-%d %H:%M:%S.%f'), '%Y-%m-%d %H:%M:%S.%f')) * 1000)
        except ValueError, e:
            logging.error("original_date = " + str(original_date) + ", " + str(e))
        product["topProductPromoInfoVendorHistory"] = tph
        upsert = {"doc": product, 'doc_as_upsert': True}
        action = make_action(id=product_id)
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

    cursor.close()
    cnx.close()


def get_all_data_from_top_product_promo_info_vendor_history(productUnit, es, esIndex, docType, pool1):
    """

    :param pool:
    :param productUnit:
    :param es:
    :param esIndex:
    :param docType:
    :return: None
    """
    total = 0
    start = 1
    end = productUnit
    num_of_products = get_all_top_product_promo_info_vendor_history(pool1)
    logging.info("Number of product in top_product_promo_info_vendor_history is " + str(num_of_products))
    while total < num_of_products:
        # queryProduct = "SELECT `product_id` " \
        #                "FROM `product` WHERE `product_id` BETWEEN {} AND {} and `deleted`=0".format(start, end)
        # cnx = pool1.connection()
        # cursor = cnx.cursor()
        # cursor.execute(queryProduct)
        # logging.info("products this time get is " + str(cursor.rowcount))
        # logging.info("Start: " + str(start) + ", End: " + str(end))

        # if cursor.rowcount != 0:
        #     for (product_id) in cursor:
        total = total + 1
        get_top_product_promo_info_vendor_history(pool1, es, esIndex, docType, start, end)
        # cursor.close()
        # cnx.close()

        start = end + 1
        end = end + productUnit


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
                        "fields": ["brands"]
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
            if isinstance(res, dict):
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


def index_create(es_client, index_name, index_mappings):
    try:
        return es_client.indices.create(index_name, index_mappings)
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
    logging.basicConfig(filename='import_top_product_promo_info_vendor_history.log', level=logging.INFO,
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

    parser.add_argument('--productUnit', default='5000')
    # parser.add_argument('--esHostPort', default='172.18.0.2:9200')
    # parser.add_argument('--esCluster', default='es-cluster')
    parser.add_argument('--esHostPort', default='192.168.1.106:9201')
    parser.add_argument('--esCluster', default='data-store')
    parser.add_argument('--esIndex', default='top_vendor_history')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--docType', default='items')

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

    index_mappings = {
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "analyzer_keyword": {
                            "type": "custom",
                            "tokenizer": "keyword",
                            "filter": "lowercase"
                        },
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "my_tokenizer",
                            "filter": ["english_possessive_stemmer", "lowercase", "english_stop", "english_stemmer"]
                        },
                        "default": {
                            "type": "custom",
                            "tokenizer": "my_tokenizer",
                            "filter": ["english_possessive_stemmer", "lowercase", "english_stop", "english_stemmer"]
                        }
                    },
                    "tokenizer": {
                        "my_tokenizer": {
                            "token_chars": ["letter", "digit"],
                            "type": "standard"
                        }
                    },
                    "filter": {
                        "english_stop": {
                            "type": "stop",
                            "stopwords": "_english_"
                        },
                        "english_stemmer": {
                            "type": "stemmer",
                            "language": "english"
                        },
                        "english_possessive_stemmer": {
                            "type": "stemmer",
                            "language": "possessive_english"
                        },
                        "my_stemmer": {
                            "type": "stemmer",
                            "language": "english"
                        }
                    }

                }
            }
        },
        "mappings": {
            "items": {
                "properties": {
                    "productId": {
                        "type": "long"
                    },
                    "topProductPromoInfoVendorHistory": {
                        "type": "nested",
                        "properties": {
                            "all": {
                                "type": "text",
                                "analyzer": "my_analyzer",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                }
                            },
                            "id": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "vendorId": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "vendor": {
                                "type": "text",
                                "analyzer": "my_analyzer",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "taskId": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "titleEn": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "titleCh": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "descEn": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "descCh": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "shareTitleEn": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "shareTitleCh": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "shareDescEn": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "shareDescCh": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all"
                            },
                            "imgUrl": {
                                "type": "text",
                                "index": "not_analyzed",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "cardWidth": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "cardHeight": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "topPrice": {
                                "properties": {
                                    "min": {
                                        "type": "float",
                                        "index": "not_analyzed",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword"
                                            }
                                        }
                                    },
                                    "max": {
                                        "type": "float",
                                        "index": "not_analyzed",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword"
                                            }
                                        }
                                    }
                                }
                            },
                            "price": {
                                "type": "text",
                                "index": "not_analyzed",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "startDate": {
                                "type": "date",
                                "format": "epoch_millis",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "endDate": {
                                "type": "date",
                                "format": "epoch_millis",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "authorId": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "keywords": {
                                "type": "text",
                                "term_vector": "with_positions_offsets",
                                "norms": {
                                    "enabled": False
                                },
                                "analyzer": "my_analyzer",
                                "copy_to": "all",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "missedTime": {
                                "type": "date",
                                "format": "epoch_millis",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "confirmed": {
                                "type": "text",
                                "index": "not_analyzed",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "createdTime": {
                                "type": "date",
                                "format": "epoch_millis",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "confirmedTime": {
                                "type": "date",
                                "format": "epoch_millis",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "deletedTime": {
                                "type": "date",
                                "format": "epoch_millis",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "confirmerId": {
                                "type": "long",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "vendorLogoUrl": {
                                "type": "text",
                                "index": "not_analyzed"
                            }
                        }
                    },
                    "updateESTime": {
                        "type": "date",
                        "format": "epoch_millis"
                    }
                }
            }
        }
    }
    es = Elasticsearch(hosts=args.esHostPort, cluster=args.esCluster)
    res = {}
    if alias_exists(es, args.esIndex):
        res = alias_get(es, args.esIndex)

    name_a = 'top_history_a'
    name_b = 'top_history_b'

    if isinstance(res, dict):
        keys = res.keys()
    else:
        t2 = datetime.datetime.now()

        logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
        pool1.close()
        # pool2.close()
    flag = False
    if len(keys) == 0:
        new_es_name = name_a
        old_es_name = name_b
        logging.info("Create index(new) " + new_es_name)
        if index_exists(es, new_es_name):
            index_delete(es, new_es_name)
        index_create(es, new_es_name, index_mappings)
        logging.info("Put alias " + args.esIndex)
        flag = True
    else:
        old_es_name = None
        if keys is not None and len(keys) > 0:
            old_es_name = keys[0]

        if old_es_name == name_a:
            new_es_name = name_b
        else:
            new_es_name = name_a

        logging.debug("Start Importing")
        if not index_exists(es, new_es_name):
            logging.info("Create index(new) " + new_es_name)
            index_create(es, new_es_name, index_mappings)
        else:
            logging.info("Delete index(new), and recreate it")
            index_delete(es, new_es_name)
            index_create(es, new_es_name, index_mappings)

    get_all_data_from_top_product_promo_info_vendor_history(int(args.productUnit), es, new_es_name, args.docType, pool1)

    count = 0
    try:
        count = es.cat.count(index=new_es_name)
    except TransportError, e:
        logging.error(str(e))
    logging.info(count)

    if count > 1000:
        logging.info("Put Alias " + new_es_name)
        alias_put(es, args.esIndex, new_es_name)
        if not flag:
            if old_es_name is not None:
                if index_exists(es, old_es_name):
                    logging.info("Delete index(old) " + old_es_name)
                    index_delete(es, old_es_name)
    else:
        if not flag:
            logging.info("Do NOT satisfy the requirements for data sanity, delete the newly created index")
            index_delete(es, new_es_name)
        else:
            alias_put(es, args.esIndex, new_es_name)
    # alias_put(es, args.esIndex, new_es_name)
    # if old_es_name is not None:
    #     if index_exists(es, old_es_name):
    #         logging.info("Delete index(old) " + old_es_name)
    #         index_delete(es, old_es_name)

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
    pool1.close()