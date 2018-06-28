#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
import MySQLdb
import datetime
import argparse
import MySQLdb
from DBUtils.PooledDB import PooledDB
def string_data_sanity_check(field):
    if field is not None and field.strip() != '' and isinstance(field, basestring):
        return True
    else:
        return False

def dict_data_sanity_check(field):
    if field is not None and len(field) > 0 and isinstance(field, dict):
        return True
    else:
        return False

def int_data_sanity_check(field):
    if field is not None and isinstance(field, long):
        return True
    else:
        return False


def datetime_data_sanity_check(field):
    if field is not None:
        return True
    else:
        return False


def string_data_handler(field_name, field, prop):
    if string_data_sanity_check(field):
        prop[field_name] = field
    
    return prop

def dict_data_handler(field_name, field, prop):
    if dict_data_sanity_check(field):
        prop[field_name] = field
    
    return prop

def int_data_handler(field_name, field, prop):
    if int_data_sanity_check(field):
        prop[field_name] = field
    
    return prop


def datetime_data_handler(field_name, field, prop):
    if datetime_data_sanity_check(field):
        prop[field_name] = int(time.mktime(time.strptime(str(field), '%Y-%m-%d %H:%M:%S')) * 1000)
    
    return prop