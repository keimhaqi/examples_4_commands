import redis
import time
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
    res = redis_conn.brpop("13867.wait")
    # time.sleep()
    print(res)
# res = redis_conn.llen('linkshare.parser.onwait.queue')
# print(res)
