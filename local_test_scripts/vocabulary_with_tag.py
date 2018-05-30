# This script aims at importing categories' info into Search System's DB in order to handle search request.
import MySQLdb
from DBUtils.PooledDB import PooledDB
import argparse
import logging
import HTMLParser
import sys
import hashlib
import datetime
from elasticsearch import Elasticsearch
import socket
import time
import string
import simplejson as json

reload(sys)
sys.setdefaultencoding('utf-8')
html_parser = HTMLParser.HTMLParser()


def get_brand_id_from_product(pool1, pool2, pool3, es, indx, docType, field):
    """

    :param cnx:
    :param es:
    :param indx:
    :param docType:
    """
    queryBrands = "SELECT DISTINCT(`brand_id`) FROM `product`"
    cnx = pool2.connection()
    cursBrands = cnx.cursor()
    cursBrands.execute(queryBrands)
    for (brand_id) in cursBrands:
        if brand_id[0] is not None:
            get_brand_info_from_brands(pool1, pool2, pool3, brand_id[0], es, indx, docType, field)
    cursBrands.close()
    cnx.close()

def handle_alias(pool1, pool2, pool3, words, field, language, alias, autonym, es, indx, docType):
    if words is not None:
        words = str(words).strip()
        if words != '':
            words = str(html_parser.unescape(words)).lower()
            return handle_words(pool1, pool2, pool3, words, field, language, alias, autonym, es, indx, docType)

# read table brands in database : jinbag on server 96.90.248.212
def get_brand_info_from_brands(pool1, pool2, pool3, brand_id, es, indx, docType, field):
    """

    :param cnx:
    :param brand_id:
    :param es:
    :param indx:
    :param docType:
    """
    queryBrands = "SELECT `brand_id`, `brand_name` , `alias_c1`, `alias_c2`, `alias_e1`, `alias_e2`, `alias_e3` FROM `brands` WHERE `brand_id`={}".format(brand_id)
    cnx1 = pool2.connection()
    cursBrands = cnx1.cursor()
    cursBrands.execute(queryBrands)
    for (brand_id, brand_name, alias_c1, alias_c2, alias_e1, alias_e2, alias_e3) in cursBrands:
        vid = handle_alias(pool1, pool2, pool3, brand_name, field, "en", 0, 0, es, indx, docType)
        handle_alias(pool1, pool2, pool3, alias_c1, field, "zh", 1, vid, es, indx, docType)
        handle_alias(pool1, pool2, pool3, alias_c2, field, "zh", 1, vid, es, indx, docType)
        handle_alias(pool1, pool2, pool3, alias_e1, field, "en", 1, vid, es, indx, docType)
        handle_alias(pool1, pool2, pool3, alias_e2, field, "en", 1, vid, es, indx, docType)
        handle_alias(pool1, pool2, pool3, alias_e3, field, "en", 1, vid, es, indx, docType)

    cursBrands.close()
    cnx1.close()

def get_vid_from_Vocabulary(pool, words, field):
    words = MySQLdb.escape_string(words)
    cnx = pool.connection()
    queryWords = "SELECT vid FROM `SysVocabulary` WHERE `words`='{}' AND `field`='{}'".format(words, field)
    cursor = cnx.cursor()
    cursor.execute(queryWords)
    vi = -1
    for (vid) in cursor:
        vi = vid[0]
    cursor.close()
    cnx.close()
    return vi

def insert_into_Vocabulary(pool, words, field, language, analyzed, sha1, alias, autonym, es, indx, docType):
    cnx = pool.connection()
    words = MySQLdb.escape_string(words)
    analyzed = MySQLdb.escape_string(analyzed)
    insertSql = "INSERT INTO `SysVocabulary` (`words`, `field`, `sha1`, `channel`, `language`, `analyzed`, `alias`, `autonym`) " \
                "VALUES ('{}', '{}', '{}', {}, '{}', '{}', {}, {})".format(words, field, sha1, 1, language, analyzed, alias, autonym)
    logging.info(insertSql)
    insertCursor = cnx.cursor()
    insertCursor.execute(insertSql)
    insertCursor.close()
    cnx.commit()
    cnx.close()

def handle_words(pool1, pool2, pool3, words, fied, language, alias, autonym, es, indx, docType):
    body = {}
    body["analyzer"] = "my_analyzer"
    body["text"] = words
    anayzed = es.indices.analyze(index=indx, body=json.dumps(body))
    tmp = []
    for it in anayzed['tokens']:
        tmp.append(it['token'])

    res = (' ').join(tmp)
    sha1 = hashlib.sha1(res).hexdigest()
    queryWords = "SELECT * FROM `SysVocabulary` WHERE `sha1`='{}' ".format(sha1)
    cnx = pool1.connection()
    cursor = cnx.cursor()
    cursor.execute(queryWords)

    vid = 0
    if cursor.rowcount > 0:
        fieldName = []
        for (vid, words, field, sha1, channel, language, analyzed, alias, autonym) in cursor:
            vid = vid
            if field not in fieldName:
                fieldName.append(field)

        if fied in fieldName:
            if alias == 0:
                prop = {}
                prop["words"] = words
                prop["field"] = fied
                prop["language"] = language
                prop["channel"] = 1
                es.index(index=indx, doc_type=docType, id=words, body=prop)
        else:
            insert_into_Vocabulary(pool1, words, fied, language, res, sha1, alias, autonym, es, indx, docType)
            if alias == 0:
                vid = get_vid_from_Vocabulary(pool1, words, fied)
                prop = {}
                prop["words"] = words
                prop["field"] = fied
                prop["language"] = language
                prop["channel"] = 1
                es.index(index=indx, doc_type=docType, id=words, body=prop)

    else:
        insert_into_Vocabulary(pool1, words, fied, language, res, sha1, alias, autonym, es, indx, docType)
        if alias == 0:
            vid = get_vid_from_Vocabulary(pool1, words, fied)
            prop = {}
            prop["words"] = words
            prop["field"] = fied
            prop["language"] = language
            prop["channel"] = 1
            es.index(index=indx, doc_type=docType, id=words, body=prop)
    cursor.close()
    cnx.close()
    if vid is None:
        vid = 0
    return vid

def get_vendor_infos(pool1, pool2, pool3, vid, es, indx, docType, field):
    queryVendorInfo = "SELECT `vendor_id`, `vendor_name_en`, `vendor_name_ch` FROM vendor WHERE `vendor_id`={}".format(vid)
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(queryVendorInfo)
    for (vendor_id, vendor_name_en, vendor_name_ch) in cursor:
        vid = handle_alias(pool1, pool2, pool3, vendor_name_en, field, "en", 0, 0, es, indx, docType)
        handle_alias(pool1, pool2, pool3, vendor_name_ch, field, "zh", 1, vid, es, indx, docType)
    cursor.close()
    cnx.close()

def get_vendor_id_from_product(pool1, pool2, pool3, es, indx, docType, field):
    queryVendors = "SELECT DISTINCT(`source_id`) FROM `product`"
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(queryVendors)
    for vendor_id in cursor:
        get_vendor_infos(pool1, pool2, pool3, vendor_id[0], es, indx, docType, field)

    cursor.close()
    cnx.close()
def get_category_id_from_product(pool1, pool2, pool3, es, indx, docType, field):
    queryCategory = "SELECT DISTINCT(`category_type_id`) FROM `product`"
    cnx = pool2.connection()
    cursor = cnx.cursor()
    cursor.execute(queryCategory)
    for cid in cursor:
        # get_vendor_infos(pool1, pool2, pool3, vendor_id[0], es, indx, docType, field)
        categories = get_category_info_from_category_tree(pool2, cid[0])
        for cat in categories:
            handle_alias(pool1, pool2, pool3, cat, field, "zh", 0, 0, es, indx, docType)

    cursor.close()
    cnx.close()

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

def make_query_body(letter):
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
                "should": {
                    "multi_match": {
                        "query": letter,
                        "fields": ["words"]
                    }
                }
            }
        }
    }
    return query_body

def get_user_tag(pool, tag_id):
    query = "SELECT `tag_id`, `user_id` FROM `user_tag` WHERE `tag_id`={}".format(tag_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    user_ids = []
    if cursor.rowcount != 0:
        for (tag_id, user_id) in cursor:
            if user_id is not None:
                user_ids.append(user_id)
    
    cursor.close()
    cnx.close()
    return user_ids


def get_tag(pool1, pool2, pool3, field, language, es, indx, doc_type):
    query = "SELECT `tag_id`, `tag_name` FROM `tag` WHERE `type`=1"
    cnx = pool2.connection()
    cursor = cnx.cursor()

    cursor.execute(query)

    if cursor.rowcount != 0:
        for (tag_id, tag_name) in cursor:
            user_ids = None
            if tag_id is not None and tag_id >= 0:
                user_ids = get_user_tag(pool2, tag_id)
            if user_ids is not None and len(user_ids) != 0:
                handle_tags(pool1, pool2, pool3, tag_name, user_ids, field, language, es, indx, doc_type)
                # handle tag autocomplete data
    
    cursor.close()
    cnx.close()

            

def handle_tags(pool1, pool2, pool3, words, user_ids, fied, language, es, indx, docType):
    body = {}
    body["analyzer"] = "my_analyzer"
    body["text"] = words
    anayzed = es.indices.analyze(index=indx, body=json.dumps(body))
    tmp = []
    for it in anayzed['tokens']:
        tmp.append(it['token'])

    res = (' ').join(tmp)
    # vid = get_vid_from_Vocabulary(pool1, words, fied)
    prop = {}
    prop["words"] = words
    prop["field"] = fied
    prop["language"] = language
    prop["channel"] = 1
    prop["user"] = user_ids
    es.index(index=indx, doc_type=docType, id=words, body=prop)

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_vocabulary_pro_with_tag.log', level=logging.INFO,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for autucomplete.")
    # pool1, settings for reading and writing table SysVocabulary in database: jinbag on server 96.90.248.210
    # parser.add_argument('--dbbackenduser', default='searchuser')
    # parser.add_argument('--dbbackendpassword', default='Tybz-xKwe-36')
    # parser.add_argument('--dbbackendhost', default='96.90.248.210')
    parser.add_argument('--dbbackenduser', default='root')
    parser.add_argument('--dbbackendpassword', default='admin')
    parser.add_argument('--dbbackendhost', default='localhost')
    parser.add_argument('--dbbackendport', default='3306')
    parser.add_argument('--dbbackenddatabase', default='jinbag')

    # pool3, settings for reading table product_sku in database: jinbag_data on server 96.90.248.210
    # parser.add_argument('--dbdatasourceuser', default='searchuser')
    # parser.add_argument('--dbdatasourcepassword', default='Tybz-xKwe-36')
    # parser.add_argument('--dbdatasourcehost', default='96.90.248.210')
    parser.add_argument('--dbdatasourceuser', default='root')
    parser.add_argument('--dbdatasourcepassword', default='admin')
    parser.add_argument('--dbdatasourcehost', default='localhost')
    parser.add_argument('--dbdatasourceport', default='3306')
    parser.add_argument('--dbdatasourcedatabase', default='jinbag_data')

    # pool2, settings for reading table brands and vendor in database: jinbag on server 96.90.248.212
    # parser.add_argument('--dbfrontenduser', default='receng')
    # parser.add_argument('--dbfrontendpassword', default='Rjbd-yihu-75')
    # parser.add_argument('--dbfrontendhost', default='192.168.1.196')
    parser.add_argument('--dbfrontenduser', default='root')
    parser.add_argument('--dbfrontendpassword', default='admin')
    parser.add_argument('--dbfrontendhost', default='localhost')
    parser.add_argument('--dbfrontendport', default='3306')
    parser.add_argument('--dbfrontenddatabase', default='jinbag')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--esHostPort', default='localhost:9200')
    parser.add_argument('--esCluster', default='elasticsearch')
    parser.add_argument('--esIndex', default='autojinbagp')
    parser.add_argument('--docType', default='items')

    args = parser.parse_args()

    # pool1 for connections used to connect database: jinbag on server 96.90.248.210 in order to read and write table SysVocabulary
    pool1 = PooledDB(
        creator = MySQLdb,
        host = args.dbbackendhost,
        port = int(args.dbbackendport),
        user = args.dbbackenduser,
        passwd = args.dbbackendpassword,
        db = args.dbbackenddatabase,
        charset='utf8'
    )

    # pool2 for connections used to connect database: jinbag_data on server 96.90.248.212 in order to read table brands and vendor
    pool2 = PooledDB(
        creator=MySQLdb,
        host=args.dbfrontendhost,
        port=int(args.dbfrontendport),
        user=args.dbfrontenduser,
        passwd=args.dbfrontendpassword,
        db=args.dbfrontenddatabase,
        charset='utf8'
    )

    # pool3 for connections used to connect database: jinbag on server 96.90.248.210 in order to read table product_sku
    pool3 = PooledDB(
        creator=MySQLdb,
        host=args.dbdatasourcehost,
        port=int(args.dbdatasourceport),
        user=args.dbdatasourceuser,
        passwd=args.dbdatasourcepassword,
        db=args.dbdatasourcedatabase,
        charset='utf8'
    )

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
                        },
                        "auto_analyzer": {
                            "type": "custom",
                            "tokenizer": "handle",
                            "filter": ["lowercase", "english_stop"]
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
                    "words": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "autocomplete",
                        "search_analyzer": "autocomplete_search",
                        "include_in_all": True
                    },
                    "language": {
                        "type": "text",
                        "index": "not_analyzed"
                    }
                }
            }
        }
    }

    es = Elasticsearch(hosts="localhost:9200")
    res = {}
    if es.indices.exists_alias(name=args.esIndex):
        res = es.indices.get_alias(name=args.esIndex)

    name_a = 'auto_ap'
    name_b = 'auto_bp'

    flag = False
    if args.esIndex in res.keys():
        # no alias, first time to run this script on this server
        new_es_name = name_a
        logging.info("Create index(new) " + new_es_name)
        if es.indices.exists_alias(new_es_name):
            es.indices.delete(new_es_name)
        es.indices.create(new_es_name, index_mappings)
        logging.info("Put alias " + args.esIndex)
        es.indices.put_alias(new_es_name, args.esIndex)
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

        if not es.indices.exists(index=new_es_name):
            logging.info("Create index(new) " + new_es_name)
            es.indices.create(index=new_es_name, body=index_mappings)

    language = "en"
    es_name = new_es_name
    brand = "brand"
    get_brand_id_from_product(pool1, pool2, pool3, es, es_name, args.docType, brand)
    vendor = "vendors"
    get_vendor_id_from_product(pool1, pool2, pool3, es, es_name, args.docType, vendor)
    category = "categories"
    get_category_id_from_product(pool1, pool2, pool3, es, es_name, args.docType, category)
    
    index_tag_type = 'tags'
    tag_mappings = {

        "properties": {
                    "words": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "autocomplete",
                        "search_analyzer": "autocomplete_search",
                        "include_in_all": True
                    },
                    "language": {
                        "type": "text",
                        "index": "not_analyzed"
                    },
                    "user":{
                        "type": "long"
                    }
                }
    }

    es.indices.put_mapping(doc_type=index_tag_type, body=tag_mappings, index=es_name)
    tag = "tags"
    # (pool1, pool2, pool3, field, language, es, indx, doc_type)
    get_tag(pool1, pool2, pool3, [tag], language, es, es_name, index_tag_type)

    count = es.cat.count(index=new_es_name)
    logging.info(count)

    count_for_sanity_check = 0
    for it in string.lowercase:
        res = es.search(index=new_es_name, doc_type=args.docType, body=make_query_body(it))
        if res is not None and 'hits' in res.keys():
            count_for_sanity_check = count_for_sanity_check + len(res['hits'])
            # logging.info(str(count_for_sanity_check))
    logging.info(count_for_sanity_check)
    if count >= 1000 and count_for_sanity_check >= 78:
        logging.info("Put Alias " + new_es_name)
        es.indices.put_alias(new_es_name, name=args.esIndex)
        if not flag:
            if old_es_name is not None:
                if es.indices.exists(index=new_es_name):
                    logging.info("Delete index(old) " + old_es_name)
                    es.indices.delete(old_es_name)
    else:
        es.indices.delete(new_es_name)
    
    # logging.info("Put Alias " + new_es_name)
    # es.indices.put_alias(new_es_name, name=args.esIndex)
    # if not flag:
    #     if old_es_name is not None:
    #         if es.indices.exists(index=new_es_name):
    #             logging.info("Delete index(old) " + old_es_name)
    #             es.indices.delete(old_es_name)

    pool1.close()
    pool2.close()
    pool3.close()
    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
