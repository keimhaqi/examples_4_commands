import datetime
import time

def transTime(assignTime):
    """
    @summary:将给定时间转换为长整形
    @param assignTime:给定的时间     如：'2016-12-3 10:30'
    @return: timeLong 长整形时间
    """
    timeList = assignTime.replace(' ','-').replace(':','-').split('-')
    timeList = map(int,timeList)  #[2016, 12, 3, 10, 30]
    timeStr = datetime.datetime(*timeList) #2016-12-03 10:30:00
    timeLong = time.mktime(timeStr.timetuple()) #1480732200.0
    return timeLong