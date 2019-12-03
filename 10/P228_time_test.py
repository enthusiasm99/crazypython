# 在终端输入以下命令

time.asctime()      # 'Wed Dec  4 23:44:55 2019'

time.ctime(30)      # 'Thu Jan  1 08:00:30 1970'

time.gmtime()       #time.struct_time(tm_year=2019, tm_mon=12, tm_mday=4, tm_hour=15, tm_min=46, tm_sec=11, tm_wday=2, tm_yday=338, tm_isdst=0)

time.tzname     # ('中国标准时间', '中国夏令时')

time.process_time()    

'''将当前时间转换为指定格式的字符串'''
time.strftime('%Y-%m-%d %H:%M:%S')  #'2019-12-04 23:50:44'

'''将指定时间字符串恢复成struct_time对象'''
st = '2018年3月20日'
time.strptime(st, '%Y年%m月%d日')   #time.struct_time(tm_year=2018, tm_mon=3, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=79, tm_isdst=-1)


