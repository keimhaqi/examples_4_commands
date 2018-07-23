#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This script aims at importing categories' info into Search System's DB in order to handle search request.
import argparse
import logging
import HTMLParser
import sys
import hashlib
import datetime
from elasticsearch import Elasticsearch
from elasticsearch import ElasticsearchException
from elasticsearch import TransportError
from elasticsearch import helpers
import socket
import time
import string
import simplejson as json


reload(sys)
sys.setdefaultencoding('utf-8')

# es.index(index=indx, doc_type=docType, id=words, body=prop)

def insert_brochure_with_products(es_client, idx, d_type):
    products = []
    for it in range(1, 10):
        products.append(it)
        prop = {}
        prop["products"] = products
        es_client.index(index=idx, doc_type=d_type, id=it, body=json.dumps(prop))

def display_all_items(es_client, idx, d_type):
    es_result = helpers.scan(client=es_client, query={"query":{"match_all":{}}},
                             scroll='5m', index=idx, doc_type=d_type,
                             timeout="1m")
    print("----------ALL DATA----------")
    for item in es_result:
        print(item['_source'])
    print("----------------------------")


def index_exists(es_client, index_name):
    try:
        return es_client.indices.exists(index_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False

def index_delete(es_client, index_name):
    if index_name is not None:
        logging.info("Delete index(old) " + old_es_name)
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

def make_query_body(product_ids):
    # {"query": {"bool": {"should": {"match": {"products": "1 2"}}}}, "size": 10}
    query_body = {
        "size": 10,
        "query": {
            "bool": {
                "should": {
                    "match": {
                        "products": ' '.join(product_ids)
                    }
                }
            }
        }
    }
    return query_body


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_brochure.log', level=logging.INFO,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for autucomplete.")
    parser.add_argument('--esHostPort', default='192.168.1.106:9201')
    parser.add_argument('--esCluster', default='data-store')
    parser.add_argument('--esIndex', default='brochure')
    parser.add_argument('--docType', default='items')

    args = parser.parse_args()

    index_mappings = {
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "autocomplete_search": {
                            "tokenizer": "lowercase"
                        },
                        "autocomplete": {
                            "filter": ["lowercase"],
                            "tokenizer": "autocomplete"
                        },
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "handle",
                            "filter": ["english_possessive_stemmer", "lowercase", "english_stop", "english_stemmer"]
                        }
                    },
                    "tokenizer": {
                        "autocomplete": {
                            "token_chars": ["letter", "digit"],
                            "min_gram": "1",
                            "type": "edge_ngram",
                            "max_gram": "10"
                        },
                        "my_tokenizer": {
                            "token_chars": ["letter", "digit"],
                            "min_gram": "1",
                            "type": "edge_ngram",
                            "max_gram": "10"
                        },
                        "handle": {
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
                    "products": {
                        "type": "int"
                    }
                }
            }
        }
    }

    es = Elasticsearch(hosts=args.esHostPort, cluster=args.esCluster )
    res = {}
    if alias_exists(es, args.esIndex):
        res = alias_get(es, args.esIndex)

    name_a = 'brochure_a'
    name_b = 'brochure_b'

    flag = False
    if args.esIndex in res.keys():
        # no alias, first time to run this script on this server
        new_es_name = name_a
        logging.info("Create index(new) " + new_es_name)
        if index_exists(es, new_es_name):
            index_delete(es, new_es_name)
        index_create(es, new_es_name, index_mappings)
        logging.info("Put alias " + args.esIndex)
        alias_put(es, args.esIndex, new_es_name)
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
            index_create(es, new_es_name, index_mappings)

    insert_brochure_with_products(es, new_es_name, args.docType)
    display_all_items(es, new_es_name, args.docType)
    products = ['1', '2', '3', '4']
    # for it in range(1, 10):
    #     products.append(str(it))
    query_body = make_query_body(products)

    es_name = new_es_name
    logging.info("Put Alias " + new_es_name)
    alias_put(es, args.esIndex, new_es_name)
    index_delete(es, old_es_name)
    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
