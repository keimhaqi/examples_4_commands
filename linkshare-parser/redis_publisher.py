#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import time
import json
from dateutil import parser as du_parser
import datetime
redis_conn = None

# 链接redis的配置信息
settings = {
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB": 0
}

redis_conn = redis.Redis(host=settings['REDIS_HOST'],
                                      port=settings['REDIS_PORT'],
                                      db=settings["REDIS_DB"],
                                      password="onepeace")

# 13867.wait表示队列名称
linkshare_parser_queue = '13867.wait'
for item in range(100):
    redis_conn.lpush(linkshare_parser_queue, json.dumps(item))
