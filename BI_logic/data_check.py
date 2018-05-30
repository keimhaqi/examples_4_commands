from elasticsearch import Elasticsearch
import datetime
import argparse
import MySQLdb
from DBUtils.PooledDB import PooledDB
import logging
import sys
import HTMLParser
import json
import time

def get_from_product_sku_amazon(pool, product_id):
    query = "select source_product_id, id, product_price, product_sale, last_checked, num_of_reviews, score, product_url from product_sku_amazon where id={}".format(product_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    product_info = {}
    for (source_product_id, id, product_price, product_sale, last_checked, num_of_reviews, score, product_url) in cursor:
        product_info["source_product_id"] = source_product_id
        product_info["id"] = id
        product_info["product_price"] = product_price
        product_info["product_sale"] = product_sale
        product_info["last_checked"] = last_checked
        product_info["num_of_reviews"] = num_of_reviews
        product_info["score"] = score
        product_info["product_url"] = product_url

    cursor.close()
    cnx.close()
    return product_info

def get_data_point(pool, webpage_id, domain_id):
    query = "select id, webpage_id, domain_id, id4, source_type, source_id, type, content, start_time, end_time, create_time, update_time, is_enable from data_point where webpage_id='{}' and domain_id={} and type={} and is_enable={}".format(webpage_id, domain_id, 1, 1)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    data_point = {}
    for (id, webpage_id, domain_id, id4, source_type, source_id, type, content, start_time, end_time, create_time, update_time, is_enable) in cursor:
        data_point["id"] = id
        data_point["webpage_id"] = webpage_id
        data_point["domain_id"] = domain_id
        data_point["id4"] = id4
        data_point["source_type"] = source_type
        data_point["source_id"] = source_id
        data_point["type"] = type
        data_point["content"] = content
        data_point["start_time"] = start_time
        data_point["end_time"] = end_time
        data_point["update_time"] = update_time
        data_point["is_enable"] = is_enable
    
    cursor.close()
    cnx.close()
    return data_point

def get_product_amazon_price(pool, product_vendor_id):
    query = "select product_sale, final_price from product_amazon_price where product_vendor_id={}".format(product_vendor_id)
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    low_price = 66666666.66
    change = 0
    for product_sale, final_price in cursor:
        if product_sale is not None:
            if low_price > product_sale:
                low_price = product_sale
                change = 1
        if final_price is not None:
            if low_price > final_price:
                low_price = final_price
                change = 1

    cursor.close()
    cnx.close()

    if change == 1:
        return low_price
    else:
        return None

def get_only_numbers(nums):
    ret = ''
    for it in nums:
        if ord(it) >= 48 and ord(it) <= 57:
            ret = ret + it
        if ord(it) == 46:
            ret = ret + it
    if len(ret) == 0:
        ret = None
    return ret
def get_all_product_number(pool):
    """

    :param pool:
    :return: number
    """
    query_product_number = "SELECT id, id3, vendor_id, create_time, attribute_value_id FROM `raw_product` where attribute_value_id=907190"
    cnx = pool.connection()
    cursor = cnx.cursor()
    cursor.execute(query_product_number)
    print(cursor.rowcount)
    number = 0
    for (id, id3, vendor_id, create_time, attribute_value_id) in cursor:
        prd = get_from_product_sku_amazon(pool, id3)
        num_of_reviews = prd["num_of_reviews"]
        score = prd["score"]
        tmp_low_price = get_product_amazon_price(pool, id3)
        low_price = None
        if tmp_low_price is not None:
            low_price = float(tmp_low_price)

        data_point = None
        product_sale = prd["product_sale"]
        productSaleMax = None
        productSaleMin = None

        if product_sale is not None and product_sale != "" and product_sale != 'N/A':
            if '-' in product_sale:
                product_sale = product_sale.replace(' ', '')
                ps = product_sale.split('-')
                min = None
                try:
                    tmp_min = get_only_numbers(ps[0].strip()[1:])
                    if tmp_min is not None:
                        min = float(tmp_min)
                except ValueError, e:
                    continue
                max = None
                try:
                    tmp_max = get_only_numbers(ps[1].strip()[1:])
                    if tmp_max is not None:
                        max = float(tmp_max)
                except ValueError, e:
                    continue
                productSaleMax = max
                productSaleMin = min
            elif '~' in product_sale:
                product_sale = product_sale.replace(' ', '')
                ps = product_sale.split('~')
                min = None
                try:
                    tmp_min = get_only_numbers(ps[0].strip()[1:])
                    if tmp_min is not None:
                        min = float(tmp_min)
                except ValueError, e:
                    continue
                max = None
                try:
                    tmp_max = get_only_numbers(ps[1].strip()[1:])
                    if tmp_max is not None:
                        max = float(tmp_max)
                except ValueError, e:
                    continue
                productSaleMax = max
                productSaleMin = min
            else:
                min = None
                try:
                    tmp_min = get_only_numbers(product_sale.strip()[1:])
                    if tmp_min is not None:
                        min = float(tmp_min)
                except ValueError, e:
                    continue
                max = None
                try:
                    tmp_max = get_only_numbers(product_sale.strip()[1:])
                    if tmp_max is not None:
                        max = float(tmp_max)
                except ValueError, e:
                    continue
                productSaleMax = max
                productSaleMin = min

        if num_of_reviews is not None and score is not None:
            data_point = get_data_point(pool, prd["source_product_id"], 3)
        else:
            print("Product " + str(prd["id"]) + "'s num_of_reviews or score is Null. The original product's url is " + str(prd["product_url"]))

        data_point_price = None
        if data_point is not None and len(data_point) > 0:
            num = data_point["content"]
            if num is not None and num.strip() != '':
                data_point_price = float(get_only_numbers(num))
                if low_price is not None:
                    if data_point_price is not None:
                        if low_price > data_point_price:
                            low_price = data_point_price
                else:
                    if data_point_price is not None:
                        low_price = data_point_price

        if productSaleMax is not None and productSaleMin is not None:
            if productSaleMax == productSaleMin:
                if num_of_reviews > 50:
                    if score > 4.0:
                        if low_price is not None:
                            if productSaleMax - low_price <= 1 or abs(productSaleMax - low_price) / low_price <= 0.05:
                                print("Product " + str(prd["id"]) + " satifies the filter. The original product's url is " + str(prd["product_url"]))
                            else:
                                print()
                                # print("Product " + str(prd["id"]) + "'s sale is higher than history low price " + str(low_price))
                        else:
                            print()
                            # print("Product " + str(prd["id"]) + " has now history Low price. The original product's url is " + str(prd["product_url"]))
                    else:
                        print()
                        # print("Product " + str(prd["id"]) + "'s score is under or equal to 4.0. The original product's url is " + str(prd["product_url"]))
                else:
                    print()
                    # print("Product " + str(prd["id"]) + "'s num_of_reviews is under 50. The original product's url is " + str(prd["product_url"]))
            else:
                print()
                # print("Product " + str(prd["id"]) + "'s price is a range, we will taks this into account in the future. The original product's url is " + str(prd["product_url"]))
        else:
            print()
            # print("Product " + str(prd["id"]) + "has no sale. The original product's url is " + str(prd["product_url"]))
        
        
    cursor.close()
    cnx.close()
    return number

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    logging.basicConfig(filename='import_product_sku.log', level=logging.DEBUG,
                        format='%(asctime)s - PID: %(process)d - %(levelname)s - %(pathname)s - lineno:%(lineno)d, %(message)s')
    parser = argparse.ArgumentParser(description="Import product info for recommendation engine")
    parser.add_argument('--dbuser', default='searchuser')
    parser.add_argument('--dbpassword', default='Tybz-xKwe-36')
    parser.add_argument('--dbhost', default='96.90.248.210')
    parser.add_argument('--dbdatabase', default='jinbag_data')
    parser.add_argument('--dbport', default='3306')

    parser.add_argument('--numOfThread', default='30')
    parser.add_argument('--numberOfProduct', default='100')
    parser.add_argument('--esIndex', default='search')
    parser.add_argument('--fixdata', default='False')
    parser.add_argument('--docType', default='items')


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

    get_all_product_number(pool)

    pool.close