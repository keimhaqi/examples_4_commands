from elasticsearch import Elasticsearch
import datetime
import argparse
import MySQLdb
from DBUtils.PooledDB import PooledDB
import logging
import sys
import HTMLParser

html_parser = HTMLParser.HTMLParser()

reload(sys)
sys.setdefaultencoding('utf-8')

def get_top_product_promo_info_vendor(pool):
    query = "select product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en, " \
            "share_title_ch, share_desc_en, share_desc_ch, img_url, card_width, card_height, price, " \
            "start_date, end_date, author_id, keywords, missed_time, confirmed, created_time, confirmed_time, deleted_time, " \
            "confirmer_id" \
            "  from top_product_promo_info_vendor where ((start_date > end_date) or price is NULL) and confirmer_id=99"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    count = 0
    print(cursor.rowcount)
    print("------------------------")
    for (product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en,
        share_desc_ch, img_url, card_width, card_height, price, start_date, end_date, author_id, keywords, missed_time, confirmed,
         created_time, confirmed_time, deleted_time, confirmer_id)in cursor:
        # print(product_id)
        if task_id is not None:
            get_top_product_promo_info_vendor_history_fix(pool, task_id)

    cursor.close()
    cnx.close()

def recover_vendor(sql, pool):
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    cursor.close()
    cnx.commit()
    cnx.close()

def get_top_product_promo_info_vendor_history_fix(pool, task_id):
    query = "select id, product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en, " \
            "share_title_ch, share_desc_en, share_desc_ch, img_url, card_width, card_height, price, " \
            "start_date, end_date, author_id, keywords, missed_time, created_time, confirmed_time, " \
            "confirmer_id" \
            "  from top_product_promo_info_vendor_history where confirmer_id != 99 and start_date <= '2018-04-8 00:00:00' and end_date >= '2018-04-12 23:59:59' and task_id={}".format(task_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    print(cursor.rowcount)
    print("------------------------")
    for (id, product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en,
        share_desc_ch, img_url, card_width, card_height, price, start_date, end_date, author_id, keywords, missed_time,
        created_time, confirmed_time, confirmer_id)in cursor:

        insert_sql = 'UPDATE top_product_promo_info_vendor set ' \
                     'product_id={}, ' \
                     'vendor_id={}, ' \
                     'task_id={}, '.format(product_id, vendor_id, task_id)
        if title_en is not None:
            insert_sql = insert_sql + '' \
                     'title_en="{}", '.format( str(html_parser.unescape(title_en)).replace('"', ''))
        if title_ch is not None:
            insert_sql = insert_sql + '' \
                     'title_ch="{}", '.format(str(html_parser.unescape(title_ch)).replace('"', ''))
        if desc_en is not None:
            insert_sql = insert_sql + '' \
                     'desc_en="{}", '.format(str(html_parser.unescape(desc_en)).replace('"', ''))
        if desc_ch is not None:
            insert_sql = insert_sql + '' \
                     'desc_ch="{}", '.format(str(html_parser.unescape(desc_ch)).replace('"', ''))
        if share_title_en is not None:
            insert_sql = insert_sql + '' \
                     'share_title_en="{}", '.format(str(html_parser.unescape(share_title_en)).replace('"', ''))
        if share_title_ch is not None:
            insert_sql = insert_sql + '' \
                     'share_title_ch="{}", '.format(str(html_parser.unescape(share_title_ch)).replace('"', ''))
        if share_desc_en is not None:
            insert_sql = insert_sql + '' \
                     'share_desc_en="{}",'.format(str(html_parser.unescape(share_desc_en)).replace('"', ''))
        if share_desc_ch is not None:
                     'share_desc_ch="{}", '.format(str(html_parser.unescape(share_desc_ch)).replace('"', ''))
        if img_url is not None:
            insert_sql = insert_sql + '' \
                     'img_url="{}", '.format(img_url)
        if card_width is not None:
            insert_sql = insert_sql + '' \
                     'card_width={} , '.format(card_width)
        if card_height is not None:
            insert_sql = insert_sql + '' \
                     'card_height={} , '.format(card_height)
        insert_sql = insert_sql + '' \
                     'price="{}", '.format(price)
        if start_date is not None:
            insert_sql = insert_sql + '' \
                     'start_date="{}", '.format(start_date)
        if end_date is not None:
            insert_sql = insert_sql + '' \
                     'end_date="{}", '.format(end_date)
        if missed_time is not None:
            insert_sql = insert_sql + '' \
                     'missed_time="{}", '.format(missed_time)
        insert_sql = insert_sql + '' \
                     'author_id={}, '.format(author_id)
        if keywords is not None:
            insert_sql = insert_sql + '' \
                     'keywords="{}", '.format(keywords)
        insert_sql = insert_sql + '' \
                     'confirmed=1,'
        if created_time is not None:
            insert_sql = insert_sql + '' \
                     'created_time="{}", '.format(created_time)
        if confirmed_time is not None:
            insert_sql = insert_sql + '' \
                     'confirmed_time="{}", '.format(confirmed_time)
        insert_sql = insert_sql + '' \
                     'deleted_time=NULL , ' \
                     'confirmer_id={} WHERE task_id={}'.format(
                   confirmer_id, task_id)


        logging.info(insert_sql)
        recover_vendor(insert_sql, pool)


    cursor.close()
    cnx.close()

def get_top_product_promo_info_vendor_history(pool):
    query = "select id, product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en, " \
            "share_title_ch, share_desc_en, share_desc_ch, img_url, card_width, card_height, price, " \
            "start_date, end_date, author_id, keywords, missed_time, created_time, confirmed_time, " \
            "confirmer_id" \
            "  from top_product_promo_info_vendor_history where id in (15678,15666,15746,15728,15654)"#.format(task_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    print(cursor.rowcount)
    print("------------------------")
    for (id, product_id, vendor_id, task_id, title_en, title_ch, desc_en, desc_ch, share_title_en, share_title_ch, share_desc_en,
        share_desc_ch, img_url, card_width, card_height, price, start_date, end_date, author_id, keywords, missed_time,
        created_time, confirmed_time, confirmer_id)in cursor:

        insert_sql = 'UPDATE top_product_promo_info_vendor set ' \
                     'product_id={}, ' \
                     'vendor_id={}, ' \
                     'task_id={}, '.format(product_id, vendor_id, task_id)
        if title_en is not None:
            insert_sql = insert_sql + '' \
                     'title_en="{}", '.format( str(html_parser.unescape(title_en)).replace('"', ''))
        if title_ch is not None:
            insert_sql = insert_sql + '' \
                     'title_ch="{}", '.format(str(html_parser.unescape(title_ch)).replace('"', ''))
        if desc_en is not None:
            insert_sql = insert_sql + '' \
                     'desc_en="{}", '.format(str(html_parser.unescape(desc_en)).replace('"', ''))
        if desc_ch is not None:
            insert_sql = insert_sql + '' \
                     'desc_ch="{}", '.format(str(html_parser.unescape(desc_ch)).replace('"', ''))
        if share_title_en is not None:
            insert_sql = insert_sql + '' \
                     'share_title_en="{}", '.format(str(html_parser.unescape(share_title_en)).replace('"', ''))
        if share_title_ch is not None:
            insert_sql = insert_sql + '' \
                     'share_title_ch="{}", '.format(str(html_parser.unescape(share_title_ch)).replace('"', ''))
        if share_desc_en is not None:
            insert_sql = insert_sql + '' \
                     'share_desc_en="{}",'.format(str(html_parser.unescape(share_desc_en)).replace('"', ''))
        if share_desc_ch is not None:
            insert_sql = insert_sql + '' \
                     'share_desc_ch="{}", '.format(str(html_parser.unescape(share_desc_ch)).replace('"', ''))
        # if img_url is not None:
        #     insert_sql = insert_sql + '' \
        #              'img_url="{}", '.format(img_url)
        # if card_width is not None:
        #     insert_sql = insert_sql + '' \
        #              'card_width={} , '.format(card_width)
        # if card_height is not None:
        #     insert_sql = insert_sql + '' \
        #              'card_height={} , '.format(card_height)
        if product_id == 10171252:
            price = '$23.99'
        elif product_id == 10194874:
            price = '$17.99'
        elif product_id == 10228124:
            price = '$34.77'
        elif product_id == 10352062:
            price = '$22.99'
        elif product_id == 10393348:
            price = '$79.83'
        insert_sql = insert_sql + '' \
                     'price="{}", '.format(price)
        # if start_date is not None:
        #     insert_sql = insert_sql + '' \
        #              'start_date="{}", '.format(start_date)
        # if end_date is not None:
        #     insert_sql = insert_sql + '' \
        #              'end_date="{}", '.format(end_date)
        # if missed_time is not None:
        #     insert_sql = insert_sql + '' \
        #              'missed_time="{}", '.format(missed_time)
        insert_sql = insert_sql + '' \
                     'author_id={}, '.format(author_id)
        if keywords is not None:
            insert_sql = insert_sql + '' \
                     'keywords="{}", '.format(keywords)
        insert_sql = insert_sql + '' \
                     'confirmed=1,'
        # if created_time is not None:
        #     insert_sql = insert_sql + '' \
        #              'created_time="{}", '.format(created_time)
        # if confirmed_time is not None:
        #     insert_sql = insert_sql + '' \
        #              'confirmed_time="{}", '.format(confirmed_time)
        insert_sql = insert_sql + '' \
                     'deleted_time=NULL , ' \
                     'confirmer_id={} WHERE task_id={}'.format(
                   confirmer_id, task_id)


        logging.info(insert_sql)
        recover_vendor(insert_sql, pool)


    cursor.close()
    cnx.close()

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_product_sku.log', level=logging.DEBUG,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for recommendation engine")
    parser.add_argument('--dbuser', default='genie')
    parser.add_argument('--dbpassword', default='Uync-zTwe-75')
    parser.add_argument('--dbhost', default='35.160.182.63')
    parser.add_argument('--dbdatabase', default='jinbag')
    parser.add_argument('--dbport', default='3306')

    # parser.add_argument('--dbuser', default='root')
    # parser.add_argument('--dbpassword', default='admin')
    # parser.add_argument('--dbhost', default='localhost')
    # parser.add_argument('--dbdatabase', default='jinbag')
    # parser.add_argument('--dbport', default='3306')

    args = parser.parse_args()

    pool = PooledDB(
        creator=MySQLdb,
        host=args.dbhost,
        port=int(args.dbport),
        user=args.dbuser,
        passwd=args.dbpassword,
        db=args.dbdatabase,
        charset='utf8'
    )


    get_top_product_promo_info_vendor_history(pool)
    # get_top_product_promo_info_vendor(pool)

    pool.close()