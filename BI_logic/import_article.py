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


def get_all_article_number(pool):
    """

    :param pool:
    :return: number
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


def judge_none(value, field_es, properties):
    if properties is None:
        return None
    if value is not None:
        properties[field_es] = value

    return properties


def judge_time_none(value, field_es, properties):
    if value is not None:
        properties = judge_none(int(
            time.mktime(time.strptime(str(value), '%Y-%m-%d %H:%M:%S')) * 1000), field_es, properties)

    return properties

def judge_text_none(value, field_es, properties):
    if value is not None and value.strip() != '':
        properties = judge_none(value, field_es, properties)

    return properties

def get_all_data_from_article(productUnit, es, esIndex, docType, attrsType, pool1, pool2):
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
    num_of_article = get_all_article_number(pool1)
    while total < num_of_article:
        queryProduct = "SELECT `id`, `comment_count`, `content`, `down_count`, " \
                       "`down_ids`, `good`, `in_time`, `last_cmt_time`, " \
                       "`update_time`, `tags`, `title`, `top`, `up_count`," \
                       "`up_ids`, `user_id`, `view_count`, `weight`, `logo_url`, `nick_name`, `last_comment_time`, `modify_time`, `view`, `language` " \
                       "FROM `article` WHERE `id` BETWEEN {} AND {}".format(start, end)
        cnx = pool1.connection()
        cursor = cnx.cursor()
        cursor.execute(queryProduct)
        logging.info("Article this time get is " + str(cursor.rowcount))
        logging.info("Start: " + str(start) + ", End: " + str(end))
        if cursor.rowcount != 0:
            all_doc = ""
            for (id, comment_count, content, down_count, down_ids,
                 good, in_time, last_cmt_time, update_time, tags, title, top,
                 up_count, up_ids,
                 user_id, view_count, weight, logo_url, nick_name, last_comment_time,
                 modify_time, view, language
                 ) in cursor:
                logging.info("Article ==> \n id = {}, comment_count = {}, content = {}, "
                             "down_count = {}, down_ids = {}, good = {}, in_time = {}, last_cmt_time = {}, update_time = {}, tags = {},"
                             "title =  {}, top = {}, up_count = {}, up_ids = {}, user_id = {}, view_count = {},"
                             "weight = {}, logo_url = {}, nick_name = {}, last_comment_time = {}, "
                             "modify_time = {}, view = {}, language = {}"
                             .format(id, comment_count, content,
                                    down_count, down_ids, good,
                                    in_time, last_cmt_time, update_time,
                                    tags, title, top,
                                    up_count, up_ids, user_id,
                                    view_count, weight, logo_url,
                                    nick_name, last_comment_time, modify_time,
                                    view, language))
                total = total + 1
                props = {}
                props = judge_none(id, "id", props)
                props = judge_none(comment_count, "commentCount", props)
                props = judge_text_none(content, "content", props)
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

def get_count_under_index(es_client, index_name):
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
    logging.basicConfig(filename='import_article_pro.log', level=logging.DEBUG,
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
    parser.add_argument('--esIndex', default='articlesearch')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--docType', default='post')
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
                "_all": {
                    "enabled": True
                },
                "include_in_all": False,
                "properties": {
                    "id": {
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
                        "include_in_all": True,
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
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
                        "include_in_all": True,
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
                        "include_in_all": True,
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
                        "include_in_all": True,
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
                        "include_in_all": True,
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
                        "include_in_all": True,
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
                        "include_in_all": True,
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
                        "include_in_all": True,
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
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
        pool2.close()

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

    num_of_article = get_all_data_from_article(int(args.productUnit), es, new_es_name, args.docType, args.attrsType, pool1, pool2)
    sanity_count = get_count_under_index(es_client=es, index_name=new_es_name)
    if sanity_count == num_of_article:
        alias_put(es, args.esIndex, new_es_name)
        if old_es_name is not None:
            if index_exists(es, old_es_name):
                logging.info("Delete index(old) " + old_es_name)
                index_delete(es, old_es_name)
    else:
        index_delete(es_client=es, index_name=new_es_name)

    t2 = datetime.datetime.now()

    logging.info("Import Date Complete, the time this script using is " + str(t2 - t1))
    pool1.close()
    pool2.close()