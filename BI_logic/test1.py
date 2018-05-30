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


def make_action(id):
    """

    :param: id -- the unique identifier for document under elasticsearch
    :return: json object
    :desc: make json object which will be used in elasicsearch bulk api
    """
    action = {"update": {"_id": str(id)}}
    return json.dumps(action)


def get_all_article_number(pool):
    """

    :param: pool -- connection pool for mysql database
    :return: number
    :desc: get the number of total articles
    """
    query_product_number = "SELECT count(`id`) FROM `article`"
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


def get_user_info(pool, user_id):
    """

    :param: pool -- connection pool for mysql database
    :param: user_id
    :return: dict object which contains user info
    :desc: get info from user_profile for specific user
    """
    query_user = "SELECT `id`, `nick_name`, `logo_url` FROM `user_profile`"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_user)
    user = {}
    for (id, nick_name, logo_url) in cursor:
        logging.info("user_id = {}, nick_name = {}, logo_ur = {}".format(id, nick_name, logo_url))
        user = judge_none(id, "userId", user)
        user = judge_text_none(nick_name, "nickName", user)
        user = judge_text_none(logo_url, "logoUrl", user)
    cursor.close()
    cnx.close()
    return user


def judge_none(value, field_es, properties):
    """

    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info
    :desc: add field_es to properties with value as soon as the value is not None
    """
    if properties is None:
        return None
    if value is not None:
        properties[field_es] = value

    return properties


def judge_time_none(value, field_es, properties):
    """

    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info
    :desc: add field_es to properties with value as soon as the value is not None, this func
           aims at handling the time info
    """
    if value is not None:
        properties = judge_none(int(
            time.mktime(time.strptime(str(value), '%Y-%m-%d %H:%M:%S')) * 1000), field_es, properties)

    return properties

def judge_text_none(value, field_es, properties):
    """
    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info
    :desc: add field_es to properties with value
    """
    if value is not None and value.strip() != '':
        properties = judge_none(html_parser.unescape(value), field_es, properties)

    return properties

def get_all_data_from_article(productUnit, es, esIndex, docType, pool1):
    """

    :param: pool1 -- the mysql database connection pool
    :param: productUnit -- the number of article that will be imported into elasticsearch at one time
    :param: es -- the elasticsearch client
    :param: esIndex -- the index that all articles will be imported into
    :param: docType -- the type of index that all articlew will be imported into
    :return: None
    :desc: query all articles from mysql database, then make a dict object to hold all articles info, finally bulk all articles
           into elasticsearch under specific index with specific type
    """
    total = 0
    start = 1
    end = productUnit
    num_of_article = get_all_article_number(pool1)
    while total < num_of_article:
        queryProduct = "SELECT `article_id`, `comment_count`, `content`, `down_count`, " \
                       "`down_ids`, `good`, `in_time`, `last_cmt_time`, " \
                       "`update_time`, `tags`, `title`, `top`, `up_count`," \
                       "`up_ids`, `user_id`, `view_count`, `weight`, `logo_url`, `nick_name`, `last_comment_time`, `modify_time`, `view`, `language`, `original_link` " \
                       "FROM `article` WHERE `id` BETWEEN {} AND {}".format(start, end)
        cnx = pool1.connection()
        cursor = cnx.cursor()
        cursor.execute(queryProduct)
        logging.info("Article this time get is " + str(cursor.rowcount))
        logging.info("Start: " + str(start) + ", End: " + str(end))
        if cursor.rowcount != 0:
            all_doc = ""
            for (article_id, comment_count, content, down_count, down_ids,
                 good, in_time, last_cmt_time, update_time, tags, title, top,
                 up_count, up_ids,
                 user_id, view_count, weight, logo_url, nick_name, last_comment_time,
                 modify_time, view, language, original_link
                 ) in cursor:
                logging.info("Article ==> \n id = {}, comment_count = {}, content = {}, "
                             "down_count = {}, down_ids = {}, good = {}, in_time = {}, last_cmt_time = {}, update_time = {}, tags = {},"
                             "title =  {}, top = {}, up_count = {}, up_ids = {}, user_id = {}, view_count = {},"
                             "weight = {}, logo_url = {}, nick_name = {}, last_comment_time = {}, "
                             "modify_time = {}, view = {}, language = {}, original_link={}"
                             .format(id, comment_count, content,
                                    down_count, down_ids, good,
                                    in_time, last_cmt_time, update_time,
                                    tags, title, top,
                                    up_count, up_ids, user_id,
                                    view_count, weight, logo_url,
                                    nick_name, last_comment_time, modify_time,
                                    view, language, original_link))
                total = total + 1
                props = {}
                props = judge_none(article_id, "article_id", props)
                props = judge_none(comment_count, "commentCount", props)
                # props = judge_text_none(content, "content", props)
                props = judge_none(down_count, "downCount", props)
                props = judge_text_none(down_ids, "downIds", props)
                props = judge_none(good, "good", props)
                props = judge_time_none(in_time, "inTime", props)
                props = judge_time_none(last_cmt_time, "lastCmtTime", props)
                props = judge_time_none(update_time, "updateTime", props)
                props = judge_text_none(tags, "tags", props)
                props = judge_text_none(title, "title", props)
                props = judge_none(top, "top", props)
                props = judge_none(up_count, "upCount", props)
                props = judge_text_none(up_ids, "upIds", props)
                props = judge_none(user_id, "userId", props)
                props = judge_none(view_count, "viewCount", props)
                props = judge_none(weight, "weight", props)
                props = judge_text_none(logo_url, "logoUrl", props)
                props = judge_text_none(nick_name, "nickName", props)
                props = judge_time_none(last_comment_time, "lastCommentTime", props)
                props = judge_time_none(modify_time, "modifyTime", props)
                props = judge_none(view, "view", props)
                props = judge_none(language, "language", props)
                props = judge_text_none(original_link, "originalLink", props)

                # handle user info
                if user_id is not None:
                    user = get_user_info(pool1, user_id)
                    if user is not None:
                        if isinstance(user, dict):
                            if len(user) > 0:
                                props["user"] = user


                upsert = {"doc": props, 'doc_as_upsert': True}
                action = make_action(id=id)
                doc = json.dumps(upsert, use_decimal=True)
                all_doc += action + "\n" + doc + "\n"

                if all_doc.strip() != '':
                    try:
                        es.bulk(index=esIndex, doc_type=docType, body=all_doc)
                    except UnicodeDecodeError, e:
                        logging.error(id)
                        logging.error(e)
                        pass
                    except ElasticsearchException, e:
                        logging.error(id)
                        logging.error(e)

        else:
            cnx.close()

        cursor.close()
        cnx.close()
        start = end + 1
        end = end + productUnit

    return num_of_article


def index_exists(es_client, index_name):
    """

    :param: es_client -- elasticsearch client object
    :param: index_name -- an index which needs to be check the existence under elasticsearch
    :return: boolean -- true ==> index_name exists under elasticsearch, false ==> index_name does not exist under elasticsearch
    :desc: check whether the index_name exists or not
    """
    try:
        return es_client.indices.exists(index_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def index_delete(es_client, index_name):
    """

    :param: es_client -- elasticsearch client object
    :param: index_name -- an index which will be deleted under elasticsearch
    :return: boolean -- true ==> delete index_name successfully under elasticsearch, false ==> fail to delete index_name under elasticsearch
    :desc: delete index_name under elasticsearch
    """
    try:
        return es_client.indices.delete(index_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def index_create(es_client, index_name, index_mappings):
    """

    :param: es_client -- elasticsearch client object
    :param: index_name -- an index which will be created under elasticsearch
    :param: index_mapping -- the mapping information for index_name
    :return: boolean -- true ==> create index_name successfully under elasticsearch, false ==> fail to create index_name under elasticsearch
    :desc: create index_name under elasticsearch
    """
    try:
        return es_client.indices.create(index_name, index_mappings)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def alias_exists(es_client, alias_name):
    """

    :param: es_client -- elasticsearch client object
    :param: alias_name -- an alias_name which will be checked for existence under elasticsearch
    :return: boolean -- true ==> alias_name exists under elasticsearch, false ==> alias_name does not exist under elasticsearch
    :desc: check whether the alias_name exists or not
    """
    try:
        return es_client.indices.exists_alias(name=args.esIndex)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def alias_get(es_client, alias_name):
    """

    :param: es_client -- elasticsearch client object
    :param: alias_name -- an alias_name which will be get under elasticsearch
    :return: dict once the alias_name exists under elasticsearch, False once the alias_name does not exists under elasticsearch
    :desc: get the specific alias info with para -- alias_name under elasticsearch
    """
    try:
        return es_client.indices.get_alias(name=args.esIndex)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False


def alias_put(es_client, alias_name, index_name):
    """

    :param: es_client -- elasticsearch client object
    :param: alias_name -- an alias_name which will be put to index_name under elasticsearch
    :return: dict once the alias_name is put upon index_name successfully under elasticsearch, False once the alias_name can not be put upon index_name under elasticsearch
    :desc: put alias_name upon index_name
    """
    try:
        return es_client.indices.put_alias(index_name, alias_name)
    except ElasticsearchException, e:
        logging.error(str(e))
        return False

def get_count_under_index(es_client, index_name):
    """

    :param: es_client -- elasticsearch client object
    :param: index_name -- an index_name which exists under elasticsearch
    :return: the number of total articles under elasticsearch
    :desc: get the count for index_name under elasticsearch
    """
    es_count = 0
    try:
        count = es_client.cat.count(index=index_name)
        print(count)
        logging.info("Count for Index: " + index_name + " is " + count)
        if count is not None and count.strip() != '' and isinstance(count, basestring):
            try:
                es_count = int(count.split(' ')[-1])
            except ValueError, e:
                logging.error(e)
    except TransportError, e:
        logging.error(str(e))

    return es_count

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_article.log', level=logging.DEBUG,
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
    parser.add_argument('--esHostPort', default='192.168.1.106:9200')
    parser.add_argument('--esCluster', default='elasticsearch')
    parser.add_argument('--esIndex', default='articlesearch')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--docType', default='post')

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
                    "allArticle":{
                        "type": "text",
                        "analyzer": "my_analyzer"
                    },
                    "articleId": {
                        "type": "long"
                    },
                    "commentCount": {
                        "type": "long"
                    },
                    "content": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        },
                        "copy_to": "allArticle",
                    },
                    "downCount": {
                        "type": "long"
                    },
                    "downIds": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "good": {
                        "type": "int"
                    },
                    "inTime": {
                        "type": "date",
                        "format": "epoch_millis"
                    },
                    "lastCmtTime": {
                        "type": "date",
                        "format": "epoch_millis"
                    },
                    "updateTime": {
                        "type": "date",
                        "format": "epoch_millis"
                    },
                    "tags": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "title": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "top": {
                        "type": "int"
                    },
                    "upCount": {
                        "type": "int"
                    },
                    "upIds": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "userId": {
                        "type": "int"
                    },
                    "viewCount": {
                        "type": "int"
                    },
                    "weight": {
                        "type": "float"
                    },
                    "logoUrl": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "nickName": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "down": {
                        "type": "int"
                    },
                    "tag": {
                        "type": "text",
                        "term_vector": "with_positions_offsets",
                        "norms": {
                            "enabled": False
                        },
                        "analyzer": "my_analyzer",
                        "copy_to": "allArticle",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "originalLink":{
                        "type": "text"
                    },
                    "up": {
                        "type": "int"
                    },
                    "lastCommentTime": {
                        "type": "date",
                        "format": "epoch_millis"
                    },
                    "modifyTime": {
                        "type": "date",
                        "format": "epoch_millis"
                    },
                    "view": {
                        "type": "int"
                    },
                    "language": {
                        "type": "int"
                    }
                }
            }
        }
    }
    es = Elasticsearch(hosts=args.esHostPort, cluster=args.esCluster)
    res = {}
    if alias_exists(es, args.esIndex):
        res = alias_get(es, args.esIndex)

    name_a = 'article_b'
    name_b = 'article_a'

    if isinstance(res, dict):
        keys = res.keys()
    else:
        t2 = datetime.datetime.now()

        logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
        pool1.close()

    flag = False
    if len(keys) == 0:
        new_es_name = name_a
        old_es_name = name_b
        logging.info("Create index(new) " + new_es_name)
        if index_exists(es, new_es_name):
            index_delete(es, new_es_name)
        index_create(es, new_es_name, index_mappings)
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

    num_of_article = get_all_data_from_article(int(args.productUnit), es, new_es_name, args.docType, pool1)
    sanity_count = get_count_under_index(es_client=es, index_name=new_es_name)
    if sanity_count == num_of_article:
        logging.info("Sanity Check Succeed, num_of_article is equal to sanity_count ==> num_of_article: " + str(num_of_article) + ", sanity_count: " + str(sanity_count))
        alias_put(es, args.esIndex, new_es_name)
        if old_es_name is not None:
            if index_exists(es, old_es_name):
                logging.info("Delete index(old) " + old_es_name)
                index_delete(es, old_es_name)
    else:
        logging.info("Sanity Check Failed, num_of_article isn't equal to sanity_count ==> num_of_article: " + str(num_of_article) + ", sanity_count: " + str(sanity_count))
        logging.info("Delete the newly created index ==> new_es_name : " + new_es_name)
        index_delete(es_client=es, index_name=new_es_name)

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
    pool1.close()