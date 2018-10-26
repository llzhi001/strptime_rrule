__author__ = 'llzhi'

import datetime
date_list = []
begin_date = '2018-09-01'
end_date = '2018-10-01'
begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
while begin_date <= end_date:
    date_str = begin_date.strftime("%Y-%m-%d")
    date_list.append(date_str)
    begin_date += datetime.timedelta(days=1)
print(date_list)

from datetime import datetime
from dateutil.rrule import rrule, DAILY
start_day = datetime(2018, 8, 17)
end_day = datetime(2018, 9, 18)
for dt in rrule(DAILY, dtstart=start_day, until=end_day):
    print(dt.strftime("%Y-%m-%d"))
