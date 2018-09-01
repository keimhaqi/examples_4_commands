#!/usr/bin/python
# -*- coding: UTF-8 -*-


import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file_object = open('./info.log')

wbk = xlwt.Workbook(encoding='utf-8')
sheet = wbk.add_sheet('sheet 1')
sheet.col(0).width = 256 * 50
sheet.col(1).width = 256 * 50
sheet.col(2).width = 256 * 50
sheet.col(3).width = 256 * 50
sheet.col(4).width = 256 * 50
sheet.col(5).width = 256 * 50
#
sheet.write(0, 0, 'SearchTime(单位:ms)')
sheet.write(0, 1, 'ElasticSearchQueryTime(单位:ms)')
sheet.write(0, 2, "Today'sPicksTime(单位:ms)")

count_4_search_time = 1
count_4_es_time = 1
count_4_today_picks_time = 1

# ProductId:1611116|ESScore:9.6904745|URScore:0|TopProduct:1|Discount:5.0
for line in file_object:
    data = line.split('|')
    if len(data) == 5:
        for element in data:
            ele = element.split(':')
            if(ele[0].__eq__('ProductId')):
                # print(data[1])1
                sheet.write(count_4_search_time, 0, data[1])
                count_4_search_time = count_4_search_time + 1
            if(ele[0].__eq__('ElasticSearchTime')):
                sheet.write(count_4_es_time, 1, data[1])
                count_4_es_time = count_4_es_time + 1
            if(data[0].__eq__("Today'sPicksTime")):
                sheet.write(count_4_today_picks_time, 2, data[1])
                count_4_today_picks_time = count_4_today_picks_time + 1
    # print(line)

wbk.save('search.xls')