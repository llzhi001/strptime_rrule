#时间格式化遍历
#strptime,将字符串转换为时间元组
#rrule(self, freq, dtstart=None, interval=1, wkst=None,count=None, until=None, bysetpos=None,

       bymonth=None, bymonthday=None, byyearday=None, byeaster=None,byweekno=None, byweekday=None, byhour=None, byminute=None, bysecond=None,cache=False)
参数理解freq:可以理解为单位。可以是 YEARLY, MONTHLY, WEEKLY,DAILY, HOURLY, MINUTELY, SECONDLY。即年月日周时分秒。
dtstart,until:是开始和结束时间。
