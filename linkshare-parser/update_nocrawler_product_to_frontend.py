import argparse
import MySQLdb
from DBUtils.PooledDB import PooledDB
import logging
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')



if __name__ == '__main__':
    t1 = datetime.datetime.now()
    parser = argparse.ArgumentParser(description="Import product3 with upc info for unpopular search.")
    # parser.add_argument('--dbbackenduser', default='searchuser')
    # parser.add_argument('--dbbackendpassword', default='Tybz-xKwe-36')
    # parser.add_argument('--dbbackendhost', default='192.168.1.193')
    # parser.add_argument('--dbbackendport', default='3306')
    # parser.add_argument('--dbbackenddatabase', default='jinbag_data')

    parser.add_argument('--dbbackenduser', default='root')
    parser.add_argument('--dbbackendpassword', default='admin')
    parser.add_argument('--dbbackendhost', default='localhost')
    parser.add_argument('--dbbackendport', default='3306')
    parser.add_argument('--dbbackenddatabase', default='jinbag_data')