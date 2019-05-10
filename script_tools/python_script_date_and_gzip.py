#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ftplib import FTP
import ftplib
import logging
import re
import os
import paramiko
from scp import SCPClient
import time
import argparse
import urllib2
import socket
import json
import signal
import redis
import datetime
from dateutil import parser as du_parser
import gzip
import cStringIO
import sys
import glob
reload(sys)
sys.setdefaultencoding('utf-8')

redis_conn = None

pattern_number_of_products = r'>([0-9]+)<'
pattern_number_of_products_compile = re.compile(pattern_number_of_products)

child_file_last_line_pattern = "<trailer><numberOfProducts>{}</numberOfProducts></trailer></merchandiser>"

max_number_of_child_file = 1000

file_name_cmp_pattern = "cmp.xml.gz"
file_name_cmp_delta_pattern = "cmp_delta.xml.gz"

def transTime(assignTime):
    """
    @summary:将给定时间转换为长整形
    @param assignTime:给定的时间     如：'2016-12-3 10:30'
    @return: timeLong 长整形时间
    """
    timeList = assignTime.replace(' ','-').replace(':','-').split('-')
    timeList = map(int,timeList)  #[2016, 12, 3, 10, 30]
    timeStr = datetime.datetime(*timeList) #2016-12-03 10:30:00
    timeLong = time.mktime(timeStr.timetuple()) #1480732200.0
    return timeLong

def call_parser_api(dir, fileName):
    # logging.info("Start to call linkshare API {}".format(fileName))
    # url = 'http://192.168.1.192:8089/parser?filename=/home/zhenping/weekNewData/{}'.format(fileName)
    # logging.info("url = {}".format(url))
    # req = urllib2.Request(url)
    # resp = None
    # count = 0
    # while True and count < 5:
    #     try:
    #         resp = urllib2.urlopen(req, timeout=3)
    #         break
    #     except Exception, error:
    #         logging.error("Cannot remove service instance! {}".format(str(error)))
    #     count = count + 1
    # if resp is not None:
    #     response = resp.read()
    #     logging.info(response)
    #     logging.info("Call Linkshare API is over.")
    redis_key_value = {}
    file_dir_on_dest = "{}".format(fileName)
    serial_number = get_serial_number_in_redis(dir)
    original_date = du_parser.parse(str(datetime.datetime.now()))
    upload_time = original_date.strftime('%Y-%m-%d %H:%M:%S.%f')

    redis_key_value["uploadTime"] = upload_time
    redis_key_value["serialNumber"] = serial_number
    redis_key_value["filename"] = file_dir_on_dest

    wait_queue = str(dir) + ".fail"

    redis_conn.lpush(wait_queue, json.dumps(redis_key_value))


def get_serial_number_in_redis(dir):
    result = redis_conn.exists(dir + ".counter")
    serial_number = 0
    if result == 0:
        redis_conn.set(dir + ".counter", 1)
        serial_number = 1
    else:
        serial_number = redis_conn.incr(dir + ".counter", 1)
    
    return serial_number


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
    child_file_names = []
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
                child_file_names.append(child_file_name)
                child_file = gzip.open(child_file_name, "wb")
                child_file.write(file_head)
                for _ in range(0, max_number_of_child_file):
                    child_file.write(xml_file_in_memory.readline())
                child_file.write(child_file_last_line_pattern.format(max_number_of_child_file))
                child_file.close()
            else:
                child_file_name = "{}{}_{}".format(file_name_head, item, file_name_tail)
                child_file_names.append(child_file_name)
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
    return child_file_names


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


def judge_list_only(value):
    if value is not None and isinstance(value, list) and len(value) > 0:
        return True
    
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


def split_large_file_into_small_file(file_name):
    child_file_names = None
    number_of_products = get_number_of_products_from_linkshare_file(file_name)
    if judge_int_only(number_of_products):
        if number_of_products > max_number_of_child_file:
            number_of_child_file = number_of_products / max_number_of_child_file + 1
            # print(number_of_child_file)
            child_file_names = make_child_file(file_name, number_of_child_file, number_of_products)
    
    return child_file_names


def transfer_file(localpath, remotepath):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("localpath : {}".format(localpath))
    logging.info("remotepath: {}".format(remotepath))
    while True:
        try:
            ssh.connect('localhost', username='zhenping', password='jzp19910307jzp', timeout=60)
            break
        except paramiko.SSHException, error:
            logging.error(error.message)
            logging.error("Some bad happened while connecting 210 server.")
    scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
    scpclient.put(localpath, remotepath)
    scpclient.close()
    ssh.close()


def read_specific_file_between_specific_time(min_time, max_time, directory_backup):
    counter = 0
    for root, dirs, files in os.walk(directory_backup):
        dir_list = sorted(files, key=lambda x: os.path.getmtime(os.path.join(directory_backup, x)), reverse=True)
        for file in dir_list:
            f = os.path.join(root, file)
            file_time = os.path.getmtime(f)
            if file_time > min_time and file_time < max_time:
                # /home/zhenping/weekNewData/macys/3184_3281764_94_Apr-04-19-18-11-47_3_cmp_delta.xml.gz
                tmp_file_name = f.split(directory_backup)

                dateInfo = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                if len(tmp_file_name) > 1:
                    file_name = tmp_file_name[1]
                    vendor_id = file_name.split('_')[0]
                    vendor_id = vendor_id.replace('/', '')
                    # # print("{}, {}".format(vendor_id, f))

                    # # 添加大文件分割动作
                    # child_file_names = split_large_file_into_small_file(f)
                    # logging.info(str(child_file_names))
                    # if not judge_list_only(child_file_names):
                    #     transfer_file(f, '/home/zhenping/weekNewData/tmp' + file_name)
                    #     call_parser_api(vendor_id, '/home/zhenping/weekNewData/tmp' + file_name)
                    # else:
                    #     for child_file_name in child_file_names:
                    #         child_file_name_info = child_file_name.split("/home/zhenping/gitlab/rakuten/bloomingdales" + "/")
                    #         if judge_list_only(child_file_name_info) and len(child_file_name_info) > 1:
                    #             child_file_name_without_dir = child_file_name_info[1]
                    #             fileName = child_file_name_without_dir.split('_')
                    #             # fileName = '_'.join(fileName[0:3]) + '_' + dateInfo + '_' + '_'.join(fileName[3:])
                    #             transfer_file(child_file_name, '/home/zhenping/weekNewData/tmp')
                    #             call_parser_api(vendor_id, '/home/zhenping/weekNewData/tmp/' + child_file_name_without_dir)
                    if vendor_id == "13867":
                        counter = counter + 1
                        logging.info("filename : {}".format(str(f)))
                        call_parser_api(vendor_id, f)
        
        # print("---------------------------------------")


def get_file_list(file_path): 
    dir_list = os.listdir(file_path) 
    if not dir_list: 
        return 
    else: 
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列 
        # # os.path.getmtime() 函数是获取文件最后修改时间 
        # # os.path.getctime() 函数是获取文件最后创建时间 
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)), reverse=True) # 
        # print(dir_list) 
        return dir_list


# import os, glob, time
 
# def search_all_files_return_by_time_reversed(path, reverse=True):
#  return sorted(glob.glob(os.path.join(path, '*')), key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=reverse)

if __name__ == '__main__':
    logging.basicConfig(filename='reparse_downloaded.log', level=logging.DEBUG,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info from linkshare")
    parser.add_argument('--dest', default='/home/zhenping/weekNewData')
    # parser.add_argument('--redis_host', default='96.90.248.210')
    parser.add_argument('--redis_host', default='localhost')
    parser.add_argument('--redis_port', default='6379')
    parser.add_argument('--redis_db', default='0')
    parser.add_argument('--redis_password', default='onepeace')

    args = parser.parse_args()

    redis_conn = redis.Redis(host=args.redis_host,
                                      port=int(args.redis_port),
                                      password=args.redis_password,
                                      db=int(args.redis_db))


    directory_backup = args.dest

    min_time = transTime('2019-04-14 00:00:00')

    max_time = transTime('2019-05-11 00:00:00')

    read_specific_file_between_specific_time(min_time, max_time, directory_backup)

    # dir_list = get_file_list(directory_backup)




    

