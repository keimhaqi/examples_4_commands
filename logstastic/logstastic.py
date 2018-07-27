#!/usr/bin/python
# -*- coding: UTF-8 -*-


import xlwt
import sys
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf-8')




STAT = 0
SearchStartTime = 0
ElasticSearchQueryStart = 0
ElasticSearchQueryEnd = 0
SearchEndTime = 0
wbk = xlwt.Workbook(encoding='utf-8')
sheet = wbk.add_sheet('sheet 1')
sheet.col(0).width = 256 * 50
sheet.col(1).width = 256 * 50
sheet.col(2).width = 256 * 50
sheet.col(3).width = 256 * 50


sheet.write(0, 0, 'v3MetricsProductStartTime(单位:ms)')
sheet.write(0, 1, 'v3MetricsProductEndTime(单位:ms)')
sheet.write(0, 2, 'v3MetricsProductTIME(单位:ms)')
sheet.write(0, 3, '/v3/metrics/product_ElasticSearchQueryStart(单位:ms)')
sheet.write(0, 4, '/v3/metrics/product_ElasticSearchQueryEnd(单位:ms)')
sheet.write(0, 5, '/v3/metrics/product_ElasticSearchTime(单位:ms)')

# def string_toDatetime(string):
#     return datetime.strptime(string, "%Y-%m-%d-%H")

count = 1
count2 = 1

files = [
    "/home/zhenping/log-info-2018-06-22.0.log",
    "/home/zhenping/log-info-2018-06-22.1.log",
    "/home/zhenping/log-info-2018-06-22.2.log",
    "/home/zhenping/log-info-2018-06-22.3.log"
]
# file_object = open('/home/zhenping/log-info-2018-06-22.0.log')
for file in files:
    file_object = open(file)
    for line in file_object:
        line = line.replace('\n', '')
        strs = line.split('|')
        if STAT == 3 and strs[0] == 'v3MetricsProductEndTime':
            SearchEndTime = long(strs[1])
            sheet.write(count, 0, SearchEndTime - SearchStartTime)
            sheet.write(count, 1, ElasticSearchQueryEnd - ElasticSearchQueryStart)
            count = count + 1
            STAT = 0
        if STAT == 2 and strs[0] == 'ElasticSearchQueryEnd':
            ElasticSearchQueryEnd = long(strs[1])
            STAT = STAT + 1
        if STAT == 0 and strs[0] == '/v3/metrics/product_ElasticSearchQueryStart':
            # print(strs)
            sheet.write(count2, 3, strs[1])
            sheet.write(count2, 4, strs[3])
            sheet.write(count2, 5, int(strs[5]))
            count2 = count2 + 1
        if STAT == 0 and strs[0] == 'v3MetricsProductStartTime':
            # SearchEndTime = long(strs[1])
            sheet.write(count, 0, strs[1])
            sheet.write(count, 1, strs[3])
            sheet.write(count, 2, int(strs[5]))
            count = count + 1
            # STAT = 0
            # print(strs)
            # SearchStartTime = long(strs[1])
            # STAT = STAT + 1
        # if strs[0] == 'SearchParam':
        #     print(line)

wbk.save('search.xls')
