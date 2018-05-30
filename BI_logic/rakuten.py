from ftplib import FTP
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

def call_parser_api(fileName):
    logging.info("Start to call linkshare API")
    url = 'http://192.168.1.197:8089/parser?filename=/home/zhenping/weekNewData/{}'.format(fileName)
    req = urllib2.Request(url)
    resp = None
    count = 0
    while True and count < 10:
        try:
            resp = urllib2.urlopen(req, timeout=3)
            break
        except Exception, error:
            logging.error("Cannot remove service instance!", error)
        count = count + 1
    if resp is not None:
        response = resp.read()
        logging.info(response)
        logging.info("Call Linkshare API is over.")



if __name__ == '__main__':
    call_parser_api("/home/zhening/monitor.json")