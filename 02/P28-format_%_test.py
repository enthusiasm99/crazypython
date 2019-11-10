# %s ： 将指定变量或值使用str()函数转换为字符串
price = 100
print("the book's price is %s" % price)

user = 'Charlie'
age = '8'
print("%s is a %s years old boy." % (user, age))


num = -28
# 6表示转换后的最小宽度，默认右对齐，补充空格
print('num is（十进制） : %6i' % num)   #带符号、十进制
print('num is （十进制）: %6d' % num)   #带符号、十进制
print('num is（八进制） : %6o' % num)   #带符号、八进制
print('num is （十六进制）: %6x' % num)   #带符号、十六进制
print('num is （十六进制）: %6X' % num)   #带符号、十六进制、大写
print('num is（字符串） : %6s' % num)   #使用str()函数转换为字符串


num2 = 30
print(num2)
print('num2 is（6位，右对齐，0补齐，十进制） : %06d' % num2)
print('num2 is（带符号，0补齐，6位，右对齐，十进制） : %+06d' % num2)
print('num2 is（d对齐，6位，十进制） : %-6d' % num2)

my_value = 3.001415926535
print(my_value)
print("my_value is : %8.3f  (8位，保留3位小数，浮点数)" % my_value)
print("my_value is : %08.3f  (0补齐，8位，保留3位小数，浮点数)" % my_value)
print("my_value is : %+08.3f  (带符号，0补齐，8位，保留3位小数，浮点数)" % my_value)

the_name = 'Charlie'
# 字符串没有0补齐
print(the_name)
print('the_name is : %.3s  (保留3个字母，字符串)' % the_name)
print('the_name is : %10.2s  (10位，保留2个字母，字符串)' % the_name)
