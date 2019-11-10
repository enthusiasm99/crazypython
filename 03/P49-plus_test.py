a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)
sum_tuple = a_tuple + b_tuple
print(sum_tuple)   #  ('crazyit', 20, -1.2, 127, 'crazyit', 'fkit', 3.33)
print(a_tuple)     #未发生变化
print(b_tuple)     #未发生变化

# 两个元组相加
print(a_tuple + (-20, -30))  #  ('crazyit', 20, -1.2, -20, -30)

# 元组和列表不能相加 。以下代码会报错
# print(a_tuple + [-20, -30])

# 列表的相加同元组
a_list = [20, 30, 50, 100]
b_list = ['a', 'b', 'c']
sum_list = a_list + b_list
print(sum_list)                   # [20, 30, 50, 100, 'a', 'b', 'c']
print(a_list + ['fkit'])          # [20, 30, 50, 100, 'fkit']