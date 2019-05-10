#!/usr/bin/python
# -*- coding: UTF-8 -*-
import paramiko
from scp import SCPClient

# 登录远程服务器

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
while True:
    try:
        ssh.connect('localhost', username='zhenping', password='jzp19910307jzp', timeout=60)
        break
    except paramiko.SSHException, error:
        logging.error(error.message)