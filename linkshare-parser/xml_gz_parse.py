#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gzip
import cStringIO
from lxml import etree
from xml.dom import minidom
import sys
import re
import os

reload(sys)
sys.setdefaultencoding('utf-8')

pattern_number_of_products = r'>([0-9]+)<'
pattern_number_of_products_compile = re.compile(pattern_number_of_products)

file_name_cmp_pattern = "cmp.xml.gz"
file_name_cmp_delta_pattern = "cmp_delta.xml.gz"

max_number_of_child_file = 500

child_file_last_line_pattern = "<trailer><numberOfProducts>{}</numberOfProducts></trailer></merchandiser>"


def judge_list_only(value):
    if value is not None and isinstance(value, list) and len(value) > 0:
        return True
    
    return True


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


def judge_dict_only(value):
    """

    :param: value -- the object contains actual value
    :return: boolean 
    :desc: return True if the value is not None and of type dict, else return False.
    """    
    if value is not None and isinstance(value, dict) and len(value) > 0:
        return True
    else:    
        return False


def lastline(file_name):
    pos = 0
    last_line_of_xml_file = None
    gzip_file = gzip.open(file_name, 'rb');
    xml_file_in_memory = cStringIO.StringIO(gzip_file.read())
    while True:
        pos = pos - 1
        try:
            xml_file_in_memory.seek(pos, 2)  # 从文件末尾开始读
            if xml_file_in_memory.read(1) == '\n':
                break
        except:  # 到达文件第一行，直接读取，退出
            xml_file_in_memory.seek(0, 0)
            break

    last_line_of_xml_file = xml_file_in_memory.readline()
    xml_file_in_memory.close()
    gzip_file.close()
    return last_line_of_xml_file


def get_number_of_products_from_linkshare_file(file_name):
    number_of_product = None
    last_line = lastline(file_name)
    match = re.findall(pattern_number_of_products_compile, last_line)
    if judge_list_only(match):
        try:
            number_of_product = int(match[0])
        except ValueError, e:
            print(e)
    
    return number_of_product

# file_name : 24285_3281764_26660386_Jan-11-19-03-41-51_cmp_delta.xml.gz
# file_name : 24285_3281764_98931637_2018_11_14_17_33_37_cmp.xml.gz
def retrieve_file_name_head_and_tail(file_name):
    file_name_info = {}

    if judge_text_only(file_name):
        if file_name_cmp_delta_pattern in file_name:
            split_res = file_name.split(file_name_cmp_delta_pattern)
            if judge_list_only(split_res):
                file_name_info["file_name_head"] = split_res[0]
                file_name_info["file_name_tail"] = file_name_cmp_delta_pattern
        elif file_name_cmp_pattern in file_name:
            split_res = file_name.split(file_name_cmp_pattern)
            if judge_list_only(split_res):
                file_name_info["file_name_head"] = split_res[0]
                file_name_info["file_name_tail"] = file_name_cmp_pattern
    
    return file_name_info


def make_child_file(file_name, counter, number_of_products):
    file_name_info = retrieve_file_name_head_and_tail(file_name)
    if judge_dict_only(file_name_info):

        file_name_head = file_name_info["file_name_head"]
        file_name_tail = file_name_info["file_name_tail"]

        gzip_file = gzip.open(file_name, 'rb');
        xml_file_in_memory = cStringIO.StringIO(gzip_file.read())

        file_head = "{}".format(xml_file_in_memory.readline())

        for item in range(0, counter):
            if counter - item != 1:
                child_file_name = "{}{}_{}".format(file_name_head, item, file_name_tail)
                child_file = gzip.open(child_file_name, "wb")
                child_file.write(file_head)
                for _ in range(0, max_number_of_child_file):
                    child_file.write(xml_file_in_memory.readline())
                child_file.write(child_file_last_line_pattern.format(max_number_of_child_file))
                child_file.close()
            else:
                child_file_name = "{}{}_{}".format(file_name_head, item, file_name_tail)
                child_file = gzip.open(child_file_name, "wb")
                child_file.write(file_head)
                line = xml_file_in_memory.readline()
                while line:
                    tmp = xml_file_in_memory.readline()
                    if judge_text_only(tmp):
                        child_file.write(line)
                        line = tmp
                    else:
                        break
                    
                
                child_file.write(child_file_last_line_pattern.format(number_of_products - (counter - 1) * max_number_of_child_file))
                child_file.close()
                

        xml_file_in_memory.close()
        gzip_file.close()


def split_large_file_into_small_file(file_name):
    number_of_products = get_number_of_products_from_linkshare_file(file_name)
    if judge_int_only(number_of_products):
        if number_of_products > max_number_of_child_file:
            number_of_child_file = number_of_products / max_number_of_child_file + 1
            # print(number_of_child_file)
            make_child_file(file_name, number_of_child_file, number_of_products)


def get_size_of_dir(file_name = '.'):
    total_size = os.path.getsize(file_name)
    for item in os.listdir(file_name):
        itempath = os.path.join(file_name, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += get_size_of_dir(itempath)
    return total_size


def get_size_of_file(file_name = '.'):
    total_size = os.path.getsize(file_name)
    return total_size


def good_read(size):

    B = "B"
    KB = "KB"
    MB = "MB"
    GB = "GB"
    TB = "TB"
    UNITS = [B, KB, MB, GB, TB]
    HUMANFMT = "%f %s"
    HUMANRADIX = 1024.

    for u in UNITS[:-1]:
        if size < HUMANRADIX : return HUMANFMT % (size, u)
        size /= HUMANRADIX

    return HUMANFMT % (size,  UNITS[-1])

if __name__ == "__main__":

    path = '/home/zhenping/linkshare_ftp/FinishLine/37731/37731_3281764_83345565_cmp_delta.xml.gz'
    # path = '/home/zhenping/linkshare_ftp/FinishLine/37731/37731_3281764_99710710_cmp.xml.gz'
    # number_of_products = get_number_of_products_from_linkshare_file(path)
    split_large_file_into_small_file(path)



    # print(number_of_products)
    # file_size = get_size_of_file(path)
    # good_read_file_size = good_read(file_size)
    # print(good_read_file_size)