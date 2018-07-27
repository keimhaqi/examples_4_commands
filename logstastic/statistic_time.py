#!/usr/bin/python
# -*- coding: UTF-8 -*-


import xlwt
import sys
import os
import argparse
reload(sys)
sys.setdefaultencoding('utf-8')

wbk = xlwt.Workbook(encoding='utf-8')
sheet = wbk.add_sheet('sheet 1')
sheet.col(0).width = 256 * 50
sheet.col(1).width = 256 * 50
sheet.col(2).width = 256 * 50

sheet.col(3).width = 256 * 50
sheet.col(4).width = 256 * 50
sheet.col(5).width = 256 * 50

sheet.col(6).width = 256 * 50
sheet.col(7).width = 256 * 50
sheet.col(8).width = 256 * 50

sheet.col(9).width = 256 * 50
sheet.col(10).width = 256 * 50
sheet.col(11).width = 256 * 50

sheet.col(12).width = 256 * 50
sheet.col(13).width = 256 * 50
sheet.col(14).width = 256 * 50
#
sheet.write(0, 0, 'SearchStartTime(Datetime)')
sheet.write(0, 1, 'SearchEndTime(Datetime)')
sheet.write(0, 2, "Search Time Cost(单位:ms)")

sheet.write(0, 3, "Today'sPicksStartTime(Datetime)")
sheet.write(0, 4, "Today'sPicksEndTime(Datetime)")
sheet.write(0, 5, "Today'sPicksTime(单位:ms)")

sheet.write(0, 6, "myStoreStartTime(Datetime)")
sheet.write(0, 7, "myStoreEndTime(Datetime)")
sheet.write(0, 8, "MyStoreTime(单位:ms)")

sheet.write(0, 9, 'ElasticSearchQueryStart(Datetime)')
sheet.write(0, 10, 'ElasticSearchQueryEnd(Datetime)')
sheet.write(0, 11, "ElasticSearchTime(单位:ms)")

sheet.write(0, 12, 'V3TodayPicksStartTime(Datetime)')
sheet.write(0, 13, 'V3TodayPicksEndTime(Datetime)')
sheet.write(0, 14, "V3TodayPicksTime(单位:ms)")

count_4_search_time = 1
count_4_es_time = 1
count_4_today_picks_time = 1
count_4_my_store_time = 1
count_4_v3_todayPicks = 1

def take_time_int_account(file_object, count_4_search_time, count_4_es_time, count_4_today_picks_time,
                          count_4_my_store_time, count_4_v3_todayPicks):
    # file_object = open('./log-info-2017-11-19.0.log')
    # file_object = open(filename)
    for line in file_object:
        data = line.split(r'|')
        if(data[0].__eq__('SearchStartTime')):
            # print(data[1])
            sheet.write(count_4_search_time, 0, data[1])
            sheet.write(count_4_search_time, 1, data[3])
            sheet.write(count_4_search_time, 2, data[5].replace('\n', ''))
            count_4_search_time = count_4_search_time + 1
        if(data[0].__eq__('ElasticSearchQueryStart')):
            sheet.write(count_4_es_time, 9, data[1])
            sheet.write(count_4_es_time, 10, data[3])
            sheet.write(count_4_es_time, 11, data[5].replace('\n', ''))
            count_4_es_time = count_4_es_time + 1
        if(data[0].__eq__("Today'sPicksStartTime")):
            sheet.write(count_4_today_picks_time, 3, data[1])
            sheet.write(count_4_today_picks_time, 4, data[3])
            sheet.write(count_4_today_picks_time, 5, data[5].replace('\n', ''))
            count_4_today_picks_time = count_4_today_picks_time + 1
        if(data[0].__eq__("myStoreStartTime")):
            sheet.write(count_4_my_store_time, 6, data[1])
            sheet.write(count_4_my_store_time, 7, data[3])
            sheet.write(count_4_my_store_time, 8, data[5].replace('\n', ''))
            count_4_my_store_time = count_4_my_store_time + 1
        if(data[0].__eq__("V3SearchLinkStartTime")):
            sheet.write(count_4_v3_todayPicks, 12, data[1])
            sheet.write(count_4_v3_todayPicks, 13, data[3])
            sheet.write(count_4_v3_todayPicks, 14, data[5].replace('\n', ''))
            count_4_v3_todayPicks = count_4_v3_todayPicks + 1

    # file_object.close()
    return [count_4_search_time, count_4_es_time, count_4_today_picks_time, count_4_my_store_time, count_4_v3_todayPicks]

# res = take_time_int_account('log-info-2017-11-19.0.log', count_4_search_time, count_4_es_time, count_4_today_picks_time, count_4_my_store_time )
# count_4_search_time = res[0]
# count_4_es_time = res[1]
# count_4_today_picks_time = res[2]
# count_4_my_store_time = res[3]
# res = take_time_int_account('log-info-2017-11-20.0.log', count_4_search_time, count_4_es_time, count_4_today_picks_time, count_4_my_store_time )
# count_4_search_time = res[0]
# count_4_es_time = res[1]
# count_4_today_picks_time = res[2]
# count_4_my_store_time = res[3]
# res = take_time_int_account('log-info-2017-11-20.1.log', count_4_search_time, count_4_es_time, count_4_today_picks_time, count_4_my_store_time )
# count_4_search_time = res[0]
# count_4_es_time = res[1]
# count_4_today_picks_time = res[2]
# count_4_my_store_time = res[3]
# res = take_time_int_account('log-info-2017-11-20.2.log', count_4_search_time, count_4_es_time, count_4_today_picks_time, count_4_my_store_time )
# count_4_search_time = res[0]
# count_4_es_time = res[1]
# count_4_today_picks_time = res[2]
# count_4_my_store_time = res[3]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Import product info from linkshare")
    parser.add_argument('--dest', default='./info')
    args = parser.parse_args()

    for filename in os.listdir(args.dest):
        file_object = open(args.dest + '/' + filename)
        res = take_time_int_account(file_object, count_4_search_time,
                                    count_4_es_time, count_4_today_picks_time,
                                    count_4_my_store_time, count_4_v3_todayPicks )
        if count_4_search_time > 60000 or count_4_es_time > 60000 or count_4_my_store_time > 60000 or count_4_today_picks_time > 60000 or count_4_v3_todayPicks > 60000:
            break;

        count_4_search_time = res[0]
        count_4_es_time = res[1]
        count_4_today_picks_time = res[2]
        count_4_my_store_time = res[3]
        count_4_v3_todayPicks = res[4]
        file_object.close()

    wbk.save('search_time.xlsx')
