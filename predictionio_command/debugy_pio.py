#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from DBUtils.PooledDB import PooledDB
import simplejson as json
import sys
import datetime
import argparse
import logging


reload(sys)
sys.setdefaultencoding('utf-8')

def get_user_id(pool):
    sql = "SELECT `id` FROM `user_profile`"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)

    user_id = []
    
    if cursor.rowcount != 0:
        for id in cursor:
            user_id.append(id[0])
    

    cursor.close()
    cnx.close()

    return user_id


def judge_text_none(value):
    """
    :param: value -- the object contains actual value
    :param: field_es -- the name of specific field
    :param: properties -- dict object contains document's info
    :return: dict object containing document's info 
    :desc: add field_es to properties with value
    """
    if value is not None and isinstance(value, basestring) and value.strip() != '':
        return True

    return False


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_brochure_pro.log', level=logging.DEBUG,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for recommendation engine")

    parser.add_argument('--vendordbuser', default='root')
    parser.add_argument('--vendordbpassword', default='admin')
    parser.add_argument('--vendordbhost', default='localhost')
    parser.add_argument('--vendordbdatabase', default='jinbag')
    parser.add_argument('--vendordbport', default='3306')

    args = parser.parse_args()

    pool = PooledDB(
        creator=MySQLdb,
        host=args.vendordbhost,
        port=int(args.vendordbport),
        user=args.vendordbuser,
        passwd=args.vendordbpassword,
        db=args.vendordbdatabase,
        charset='utf8'
    )


    user_id = get_user_id(pool)

    cal_res = {}
    for it in user_id:
        cal_res[it] = 0

    events = ['view', 'plan', 'buy', 'fav']
    hbase_data = open("/home/zhenping/zhenping_07_08_2018/part-00000")
    for line in hbase_data:
        event = json.loads(line)
        if event is not None and isinstance(event, dict):
            keys = event.keys()
            if 'event' in keys:
                event_value = event['event']
                if event_value is not None and event_value.strip() in events:
                    if 'entityId' in keys:
                        entity_id = event['entityId']
                        if entity_id is not None and isinstance(entity_id, basestring) and entity_id.strip() != '':
                            try:
                                entity_id_int = int(entity_id)
                                if entity_id_int in user_id:
                                    cal_res[entity_id_int] = cal_res[entity_id_int] + 1
                            except ValueError, e:
                                print(e)
    
    hbase_data = open("/home/zhenping/zhenping_07_08_2018/part-00001")
    for line in hbase_data:
            event = json.loads(line)
            if event is not None and isinstance(event, dict):
                keys = event.keys()
                if 'event' in keys:
                    event_value = event['event']
                    if event_value is not None and event_value.strip() in events:
                        if 'entityId' in keys:
                            entity_id = event['entityId']
                            if entity_id is not None and isinstance(entity_id, basestring) and entity_id.strip() != '':
                                try:
                                    entity_id_int = int(entity_id)
                                    if entity_id_int in user_id:
                                        cal_res[entity_id_int] = cal_res[entity_id_int] + 1
                                except ValueError, e:
                                    print(e)
    for key in cal_res:
        if cal_res[key] != 0:
            print(str(key) + " : " + str(cal_res[key]))

    pool.close()