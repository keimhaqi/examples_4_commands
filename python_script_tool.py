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
import json
from elasticsearch import helpers
from decimal import Decimal
from decimal import getcontext

reload(sys)
sys.setdefaultencoding('utf-8')    

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