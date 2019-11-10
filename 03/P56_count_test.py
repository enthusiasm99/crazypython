a_list = [2, 30, 'a', [5, 30], 30]
print(a_list)
print(a_list.count(30))     #2  ，不是3
print(a_list.count([5, 30]))

b_list = [2, 30, 'a', 'b',  'crazyit', 30]
print(b_list.index(30))       # 1
print(b_list.index(30, 2))    #从索引2开始查找   结果为： 5
print(b_list.index(30, 2, 4)) #在索引2至3中查找  结果报错，找不到