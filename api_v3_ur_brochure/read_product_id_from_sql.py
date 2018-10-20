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
import math

reload(sys)
sys.setdefaultencoding('utf-8')

html_parser = HTMLParser.HTMLParser()
hash = hashlib.sha1()

def judge_none(value):
    """

    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info 
    :desc: add field_es to properties with value as soon as the value is not None
    """
    if value is not None and isinstance(value, long):
        return True
    else:
        return False

def get_product_id_from_article_product(pool):
    sql = "SELECT DISTINCT(`product_id`) FROM `article_product`"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    product_ids = []
    if cursor.rowcount != 0:
        for product_id in cursor:
            if judge_none(product_id[0]):
                product_ids.append(str(product_id[0]))
    
    cursor.close()
    cnx.close()
    return product_ids

def get_article_id_from_article(pool):
    sql = "SELECT `id` FROM `article`"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    article_ids = []
    if cursor.rowcount != 0:
        for article_id in cursor:
            if judge_none(article_id[0]):
                article_ids.append(str(article_id[0]))
    
    cursor.close()
    cnx.close()
    return article_ids

def get_article_id_from_article_product(pool):
    sql = "select distinct(product_id) from article_product as ap right join (select id, in_time from comment as co order by co.in_time) as inner_query on (ap.comment_id=inner_query.id) "
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    product_ids = []
    if cursor.rowcount != 0:
        for product_id in cursor:
            if judge_none(product_id[0]):
                product_ids.append(int(product_id[0]))
    
    cursor.close()
    cnx.close()
    return product_ids


def get_product_id_only_from_product(pool):
    sql = "select distinct(product_id) from `product`"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    product_ids = []
    if cursor.rowcount != 0:
        for product_id in cursor:
            if judge_none(product_id[0]):
                product_ids.append(int(product_id[0]))
    
    cursor.close()
    cnx.close()
    return product_ids


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='read_product_id_from_sql.log', level=logging.DEBUG,
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
    parser.add_argument('--vendordbdatabase', default='pro_jinbag')
    parser.add_argument('--vendordbport', default='3306')

    args = parser.parse_args()

    pool = PooledDB(
        creator=MySQLdb,
        host=args.vendordbhost,
        port=int(args.vendordbport),
        user=args.vendordbuser,
        passwd=args.vendordbpassword,
        db=args.vendordbdatabase,
        charset='utf8'
    )


    # article_ids = get_article_id_from_article(pool)
    # a_ids = '\npreference.brochure.'.join(article_ids)
    # for item in article_ids:
    #     print('preference.brochure.{}=0.0'.format(item))

    product_ids = get_product_id_only_from_product(pool)
    for it in product_ids:
        print(it)
    pool.close()



