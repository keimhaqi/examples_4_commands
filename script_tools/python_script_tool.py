#!/usr/bin/python
# -*- coding: UTF-8 -*-
from elasticsearch import Elasticsearch
import datetime
import argparse
import MySQLdb
from MySQLdb import escape_string
from DBUtils.PooledDB import PooledDB
import logging
import sys
import HTMLParser
import time
import hashlib
import json
from elasticsearch import helpers
from decimal import Decimal
from decimal import getcontext
from dateutil import parser as du_parser
import os

reload(sys)
sys.setdefaultencoding('utf-8')

html_parser = HTMLParser.HTMLParser()

def judge_long_only(value):
    """

    :param: value -- the object contains actual value
    :return: dict object containing document's info 
    :desc: return true if the value is not None and is of type long.
    """
    if value is not None and isinstance(value, long):
        return True
    else:
        return False

def judge_text(value, field_es, properties):
    """

    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info 
    :desc: aims at putting value into properties with the name of field_es.
    """
    if properties is None:
        properties = {}
    if value is not None and isinstance(value, basestring) and value.strip() != '':
        properties[field_es] = value
    
    return properties

def judge_text_only(value):
    """

    :param: value -- the object contains actual value
    :return: dict object containing document's info 
    :desc: return true if the value is not None and is of type string.
    """
    if value is not None and isinstance(value, basestring) and value.strip() != '':
        return True
    else:
        return False


def judge_int_only(value):
    """

    :param: value -- the object contains actual value
    :return: dict object containing document's info 
    :desc: return true if the value is not None and is of type long.
    """
    if value is not None and isinstance(value, int):
        return True
    else:
        return False


def judge_list_only(value):
    if value is not None and isinstance(value, list) and len(value) > 0:
        return True
    
    return False


def get_only_numbers(nums):
    items = ''
    for it in nums:
        if ord(it) >= 48 and ord(it) <= 57:
            items = items + it
        if ord(it) == 46:
            items = items + it
    if len(items) == 0:
        items = '0'
    return items


def judge_list(value, field_es, properties):
    if judge_list_only(value):
        properties[field_es] = value
    
    return properties


def judge_dict_only(value):
    if value is not None and isinstance(value, dict) and len(value) > 0:
        return True
    
    return False


def judge_tuple_only(value):
    if value is not None and isinstance(value, tuple) and len(value) > 0:
        return True
    
    return False


def judge_set_only(value):
    if value is not None and isinstance(value, set) and len(value) > 0:
        return True
    
    return False


def judge_none(value):
    if value is None:
        return False
    else:
        return True


def judge_decimal_only(value):
    if value is not None and isinstance(value, Decimal):
        return True
    else:
        return False


def compare_str(string1, string2):
    flag = False
    if judge_text_only(string1) and judge_text_only(string2):
        if string1.strip() == string2.strip():
            flag = True
    
    return flag

def judge_long(value, field_es, properties):
    """

    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info 
    :desc: add field_es to properties with value as soon as the value is not None
    """
    if properties is None:
        properties = {}
    if judge_long_only(value):
        properties[field_es] = value

    return properties


def judge_int(value, field_es, properties):
    """

    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info 
    :desc: add field_es to properties with value as soon as the value is not None
    """
    if properties is None:
        properties = {}
    if judge_int_only(value):
        properties[field_es] = value

    return properties


def large_text_handler(value, field_es, properties):

    if judge_text_only(value):
        if not judge_dict_only(properties):
            properties = {}
        escaped_value = html_parser.unescape(value)
        if not escaped_value.startswith('['):
            properties[field_es] = [html_parser.unescape(value)]
        else:
            properties[field_es] = escaped_value[1:-1].replace('"', '').split(',')
    
    return properties

def judge_datetime_only(value):
    if value is not None and isinstance(value, datetime.datetime):
        return True
    else:
        return False

def judge_datetime(value, field_es, properties):
    if judge_datetime_only(value):
        properties[field_es] = value
    return properties


# 获取系统中文件的mtime, f表示文件的完整路径名称, 例如: /home/zhenping/weekNewData/macys/3184_3281764_94_Apr-04-19-18-11-47_3_cmp_delta.xml.gz
f = "/home/zhenping/weekNewData/macys/3184_3281764_94_Apr-04-19-18-11-47_3_cmp_delta.xml.gz"
file_time = os.path.getmtime(f) # file_time类型为long

# 对系统中指定目录下的文件根据mtime做排序, 可以是正序或者逆序:
# files表示文件列表, 类型为list, directory_backup表示文件列表中的文件所在路径, reverse表示是否以逆序排序, True表示逆序, Fales表示正序
files = ["/home/zhenping/weekNewData/macys/3184_3281764_94_Apr-04-19-18-11-47_3_cmp_delta.xml.gz"]
directory_backup = "/home/zhenping/weekNewData/macys"
dir_list = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory_backup, x)), reverse=True)