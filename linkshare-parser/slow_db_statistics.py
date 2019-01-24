#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
pattern_number_of_products = r'([0-9]+)'
pattern_number_of_products_compile = re.compile(pattern_number_of_products)


def judge_list_only(value):
    if value is not None and isinstance(value, list) and len(value) > 0:
        return True
    
    return False


if __name__ == '__main__':
    slow_log = open("./linkshare-parser/slow_log.log")

    line = slow_log.readline()

    sum = 0
    counter = 0

    min = sys.maxint
    max = 0

    while line:
        if "向数据库写完一条记录(nordstrom)" in line:
            match = re.findall(pattern_number_of_products_compile, line)
            if judge_list_only(match):
                counter = counter + 1
                single_parse_time = int(match[-1])
                sum = sum + single_parse_time
                if single_parse_time < min:
                    min = single_parse_time
                if single_parse_time > max:
                    max = single_parse_time
        line = slow_log.readline()
    
    if sum != 0 and counter != 0:
        print("max is {}ms, min is {}ms, average is {} ms, sum is {}ms, counter is {} products.".format(max, min, sum / counter, sum, counter))