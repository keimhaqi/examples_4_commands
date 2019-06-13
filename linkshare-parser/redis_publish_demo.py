#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import time
import json
from dateutil import parser as du_parser
import datetime
redis_conn = None

linkshare_parser_queue = None
def get_serial_number_in_redis():
    result = redis_conn.exists("counter")
    serial_number = 0
    if result == 0:
        redis_conn.set('counter', 1)
        serial_number = 1
    else:
        serial_number = redis_conn.incr("counter", 1)
    
    return serial_number

def call_parser_api(fileName):
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
    # file_dir_on_dest = "/home/zhenping/weekNewData/{}".format(fileName)
    file_dir_on_dest = "/home/zhenping/github/examples_4_commands/linkshare-parser/single_demo/{}".format(fileName)
    # file_dir_on_dest = "/home/zhenping/weekNewData/tmp/{}".format(fileName)
    # file_dir_on_dest = "/home/zhenping/linkshare_ftp/{}".format(fileName)
    serial_number = get_serial_number_in_redis()
    original_date = du_parser.parse(str(datetime.datetime.now() - datetime.timedelta(days=10)))
    upload_time = original_date.strftime('%Y-%m-%d %H:%M:%S.%f')

    redis_key_value["uploadTime"] = upload_time
    redis_key_value["serialNumber"] = serial_number
    redis_key_value["filename"] = file_dir_on_dest

    redis_conn.lpush(linkshare_parser_queue, json.dumps(redis_key_value))
    # redis_conn.lpush('linkshare.parser.onwait.queue', "BBB")
    # redis_conn.flushdb()

settings = {
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB": 0
}

redis_conn = redis.Redis(host=settings['REDIS_HOST'],
                                      port=settings['REDIS_PORT'],
                                      db=settings["REDIS_DB"],
                                      password="onepeace")


# linkshare_parser_queue = '24285.wait'
# 38606_3281764_1_cmp.xml.gz
# 38606_3281764_98551_cmp.xml.gz
# call_parser_api('1')
# call_parser_api('2')
# call_parser_api('3')
# call_parser_api('4')
# call_parser_api('5')
# call_parser_api('6')
# for item in range(1, 100000):
    # print "Start : %s" % time.ctime()
    # time.sleep( 5 )
    # print "End : %s" % time.ctime()
# call_parser_api('24285_3281764_98931637_2018_11_28_12_06_12_cmp.xml.gz')

# linkshare_parser_queue = '13867.wait'
# call_parser_api('bloomingdales_13867.xml.gz')


linkshare_parser_queue = '13867.wait'
# call_parser_api('13867_3281764_1489_Apr-14-19-00-05-39_4_cmp_delta.xml.gz')
# call_parser_api('13867_3281764_26659427_Jul-04-18-11-01-58_2_cmp_delta.xml.gz') # 849683046482
# call_parser_api('13867_3281764_26659427_Feb-05-18-16-31-11_3_cmp_delta.xml.gz')
# call_parser_api('13867_3281764_26659427_Feb-05-18-16-31-11_3_cmp_delta.xml.gz')
# call_parser_api('13867_3281764_26659427_Mar-22-18-10-30-36_3_cmp_delta.xml.gz')
# call_parser_api('13867_3281764_26659427_Aug-04-18-22-02-48_6_cmp_delta.xml.gz')

linkshare_parser_queue = '3184.wait'
# call_parser_api('macys_3184.xml.gz')
# call_parser_api('3184_3281764_6_May-08-19-21-01-09_1_cmp_delta.xml.gz')
# call_parser_api('3184_3281764_6_May-08-19-21-01-09_1_cmp_delta.xml.gz')
# call_parser_api('3184_3281764_79_May-08-19-21-01-11_0_cmp_delta.xml.gz')
# call_parser_api('3184_3281764_79_May-08-19-21-01-11_1_cmp_delta.xml.gz')
# call_parser_api('3184_3281764_94_May-08-19-21-01-13_0_cmp_delta.xml.gz')
# call_parser_api('3184_3281764_94_May-08-19-21-01-13_1_cmp_delta.xml.gz')


linkshare_parser_queue = '3184.wait'
call_parser_api('demo.xml.gz')
# call_parser_api('1237_3281764_1_273_cmp.xml.gz')


# 3184_3281764_99533_May-08-19-21-01-14_cmp_delta.xml.gz


# /home/zhenping/weekNewData/tmp/13867_3281764_26659427_Jul-04-18-11-01-58_2_cmp_delta.xml.gz
# /home/zhenping/weekNewData/tmp/13867_3281764_26659427_Nov-25-17-11-30-39_4_cmp_delta.xml.gz
# /home/zhenping/weekNewData/tmp/13867_3281764_26659427_Feb-05-18-16-31-11_3_cmp_delta.xml.gz
# /home/zhenping/weekNewData/tmp/13867_3281764_26659427_Feb-05-18-16-31-11_3_cmp_delta.xml.gz
# /home/zhenping/weekNewData/tmp/13867_3281764_26659427_Mar-22-18-10-30-36_3_cmp_delta.xml.gz
# /home/zhenping/weekNewData/tmp/13867_3281764_26659427_Aug-04-18-22-02-48_6_cmp_delta.xml.gz



# linkshare_parser_queue = "38606.wait"
# call_parser_api('bestbuy_38606.xml.gz')
# for item in range(0 , 100):
#     redis_conn.lpush(linkshare_parser_queue, json.dumps(item))

# call_parser_api('24285_3281764_98931637_2018_11_28_12_06_12_81_cmp.xml.gz')
# call_parser_api('24285_3281764_98931637_2018_11_28_12_06_12_0_cmp.xml.gz')
# call_parser_api('24285_3281764_98931637_2018_11_28_12_06_12_127_cmp.xml.gz')
# call_parser_api('24285_3281764_98931637_2018_11_28_12_06_12_162_cmp.xml.gz')



# parsingQueue = "{\"42156\":{\"counter\":0},\"42157\":{\"counter\":0},\"38650\":{\"counter\":0},\"38651\":{\"counter\":0},\"36310\":{\"merchandiser\":\"dyson\",\"counter\":0},\"counterMax\":5,\"25003\":{\"merchandiser\":\"neiman marcus\",\"counter\":0},\"24895\":{\"merchandiser\":\"dillards\",\"counter\":0},\"42666\":{\"counter\":0},\"3184\":{\"merchandiser\":\"macys\",\"fileInfo\":{\"/home/zhenping/weekNewData/3184_3281764_25993792_Dec-08-18-15-00-37_cmp_delta.xml.gz\":{\"uploadTime\":\"2018-12-08 15:00:38.146421\",\"serialNumber\":189,\"filename\":\"/home/zhenping/weekNewData/3184_3281764_25993792_Dec-08-18-15-00-37_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-21 08:23:41.000825\"},\"/home/zhenping/weekNewData/3184_3281764_25993782_Dec-08-18-15-00-35_cmp_delta.xml.gz\":{\"uploadTime\":\"2018-12-08 15:00:36.180252\",\"serialNumber\":188,\"filename\":\"/home/zhenping/weekNewData/3184_3281764_25993782_Dec-08-18-15-00-35_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-21 08:20:41.000702\"},\"/home/zhenping/weekNewData/3184_3281764_25993830_Dec-08-18-15-00-47_cmp_delta.xml.gz\":{\"uploadTime\":\"2018-12-08 15:00:48.812884\",\"serialNumber\":190,\"filename\":\"/home/zhenping/weekNewData/3184_3281764_25993830_Dec-08-18-15-00-47_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-21 08:32:42.000119\"},\"/home/zhenping/weekNewData/3184_3281764_147041288_Dec-08-18-15-00-22_cmp_delta.xml.gz\":{\"uploadTime\":\"2018-12-08 15:00:23.470903\",\"serialNumber\":180,\"filename\":\"/home/zhenping/weekNewData/3184_3281764_147041288_Dec-08-18-15-00-22_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-21 06:26:37.000950\"},\"/home/zhenping/weekNewData/3184_3281764_147041192_Dec-08-18-15-00-13_cmp_delta.xml.gz\":{\"uploadTime\":\"2018-12-08 15:00:13.912006\",\"serialNumber\":178,\"filename\":\"/home/zhenping/weekNewData/3184_3281764_147041192_Dec-08-18-15-00-13_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-21 06:23:37.000830\"}},\"counter\":5},\"13816\":{\"merchandiser\":\"saks\",\"counter\":0},\"1237\":{\"merchandiser\":\"nordstrom\",\"fileInfo\":{\"/home/zhenping/weekNewData/1237_3281764_99865888_Nov-30-18-12-01-32_cmp_delta.xml.gz\":{\"uploadTime\":\"2018-11-30 12:01:33.130229\",\"serialNumber\":114,\"filename\":\"/home/zhenping/weekNewData/1237_3281764_99865888_Nov-30-18-12-01-32_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-20 03:46:44.000158\"}},\"counter\":1},\"24285\":{\"merchandiser\":\"yoox.com\",\"counter\":0},\"36025\":{\"merchandiser\":\"lastcall\",\"counter\":0},\"38655\":{\"merchandiser\":\"striderite\",\"counter\":0},\"37731\":{\"merchandiser\":\"finish line\",\"counter\":0},\"39757\":{\"merchandiser\":\"joes new balance outlet\",\"counter\":0},\"38733\":{\"counter\":0},\"39558\":{\"counter\":0},\"39756\":{\"counter\":0},\"38801\":{\"merchandiser\":\"saksoff5th\",\"fileInfo\":{\"/home/zhenping/weekNewData/38801_3281764_102416765_Jan-11-19-03-01-59_cmp_delta.xml.gz\":{\"uploadTime\":\"2019-01-11 03:02:00.155925\",\"serialNumber\":11260,\"filename\":\"/home/zhenping/weekNewData/38801_3281764_102416765_Jan-11-19-03-01-59_cmp_delta.xml.gz\",\"startParseTime\":\"2019-01-17 10:11:35.000658\"}},\"counter\":1},\"13867\":{\"merchandiser\":\"bloomingdales\",\"counter\":0},\"38606\":{\"merchandiser\":\"bestbuy\",\"counter\":0}}"
# redis_conn.set("parsingQueue", parsingQueue)
# 37731_3281764_83345565_cmp_delta.xml.gz
# for item in range(1, 1000):
# linkshare_parser_queue = '38606.wait'
# call_parser_api('38606_3281764_1_cmp.xml.gz')
# call_parser_api('1237_3281764_165094843_cmp_delta.xml.gz')
# call_parser_api('1237_3281764_165094843_cmp_delta.xml.gz')
# call_parser_api('1237_3281764_165094843_cmp_delta.xml.gz')
# call_parser_api('1237_3281764_165094843_cmp_delta.xml.gz')
# call_parser_api('1237_3281764_165094843_cmp_delta.xml.gz')
# call_parser_api('1237_3281764_165094843_cmp_delta.xml.gz')
    
# key = "linkshare.parser.queue"

# for item in range(1, 10000):
#     dic = {}
#     dic[item] = item
#     redis_conn.lpush(key, json.dumps(dic))
#     time.sleep(2)

# result = redis_conn.exists("counter")
# # print(result)

# if(result == 0):
#     redis_conn.set("counter", 1)
# else:
#     counter = redis_conn.incr("counter", 1)
#     # redis_conn.set("counter", counter)
#     print(counter)

# redis_conn.set("counter", 0)

