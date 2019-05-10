#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ftplib import FTP
import ftplib
import logging
import socket
import os


def get_ftp_client():
    ftp.connect("aftp.linksynergy.com")
    while True:
        try:
            ftp.login('jinbaginc', '0reD164G')
            break
        except Exception, error:
            logging.error(error.message)
            logging.error("Logging in error, will try again.")

    return ftp


# 从ftp服务器下载文件
def fetch_single_file(dirs):
    logging.info("Start to fetch file " + dirs)
    try:
        size = ftp.size(os.path.basename(dirs))
        if size == 0:
            return False
        file_handle = open(dirs, "w")
        # snapshot是记录的文件的大小信息;
        if len(snapshot) != 0:
            keys = snapshot.keys()
            if os.path.basename(dirs) in keys:
                if snapshot[os.path.basename(dirs)] == size:
                    return False
        logging.info("File " + dirs + "'s size is " + str(size))
        snapshot[os.path.basename(dirs)] = size
        response_code = 400
        while response_code != 226:
            try:
                ftp.retrbinary('RETR %s' % os.path.basename(dirs),file_handle.write)
                response_code = 226
            except socket.error, e:
                logging.error(e.message)
                logging.error("Some bad interrupted transferring file.")
                get_ftp_client()
        logging.info("File ==> " + dirs + " downloaded completed.")
        file_handle.flush()
        file_handle.close()
        return True
    except ftplib.error_perm, e:
        logging.error("Can not read file {}".format(e))
        return False


# 获取ftp服务器上指定文件的大小
size = ftp.size(os.path.basename(dirs))

