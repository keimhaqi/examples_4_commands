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
    file_dir_on_dest = "/home/zhenping/linkshare_ftp/FinishLine/37731/{}".format(fileName)
    serial_number = get_serial_number_in_redis()
    original_date = du_parser.parse(str(datetime.datetime.now()))
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

linkshare_parser_queue = '37731.wait'
call_parser_api('37731_3281764_100400967_cmp.xml.gz')
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

