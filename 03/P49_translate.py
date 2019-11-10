
# 注意，如果元组中只有一个元素，如'th'，必须加逗号，不然程序会将其判断为字符串，程序会报错
#1st    2nd   3rd   4-20 th    21st  22nd  23rd  24-30th   31st
order_ending = ('st', 'nd', 'rd') +  ('th',) * 17\
               + ('st', 'nd', 'rd')  + ('th',) * 7 + ('st',)
print(order_ending)

day = input("请输入日期〔1-31〕：")
day_int = int(day)

# 元组的访问，为元组名[]， 不能写为元组名([])， 如order_ending([day_int - 1])为错误写法
print(day + order_ending[day_int - 1])
