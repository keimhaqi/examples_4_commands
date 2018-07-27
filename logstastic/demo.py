from dateutil import parser
import datetime

# original_date = parser.parse(str(datetime.datetime.now()))
original_date = parser.parse('2017-12-30 12:12:53')
required_date = original_date.strftime('%Y-%m-%d %H:%M:%S.%f')

print(required_date)