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

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='repaire_todayspicks_vendors.log', level=logging.DEBUG,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for recommendation engine")

    parser.add_argument('--esHostPort', default='192.168.1.105:9201')
    parser.add_argument('--esCluster', default='data-store')
    parser.add_argument('--esIndex', default='merger_tree_v1')
    parser.add_argument('--docType', default='tree')

    args = parser.parse_args()

    es = Elasticsearch(hosts=args.esHostPort, cluster=args.esCluster)

    es_result = helpers.scan(client=es, query={"query":{"match_all":{}}},
                             scroll='5m', index=args.esIndex, doc_type=args.docType,
                             timeout="1m")
    final_result = []
    for item in es_result:
        final_result.append(item['_source'])
    
    file_write = open("/home/zhenping/github/examples_4_commands/es_command/merged_product_id.txt", "w+")
    for item in final_result:
        keys = item.keys()
        if 'productIds' in keys and item["productIds"] is not None:
            # print(item["productIds"])
            if len(item["productIds"]) > 1:
                file_write.write("{}\n".format(item["productIds"]))
    
    file_write.flush()
    file_write.close()