#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import time

# 链接redis的配置信息
settings = {
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB": 0
}

redis_conn = redis.Redis(host=settings['REDIS_HOST'],
                                      port=settings['REDIS_PORT'],
                                      db=settings.get('REDIS_DB'),
                                      password="onepeace")


while True:
    # 13867.wait是队列名称，表示从这个队列拿数据;
    res = redis_conn.brpop("13867.wait")
    # time.sleep(1)
    print(res)
