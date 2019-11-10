a_list = ['crazyit', 20, -2.4, (3, 4), 'fkit']
del a_list[2]
print(a_list)

del a_list[1:3]
print(a_list)

b_list = list(range(1, 10))
print(b_list)               # [1, 2, 3, 4, 5, 6, 7, 8, 9]
del b_list[2: -2: 2]
print(b_list)               # [1, 2, 4, 6, 8, 9]
del b_list[2: 4]
print(b_list)               # [1, 2, 8, 9]


c_list = [20, 'crazyit', 20, 30, -2.4, 'crazyit', (3, 4), 'fkit']
c_list.remove(30)   # 只删除第一个找到的元素
print(c_list)
c_list.remove(20)
print(c_list)
c_list.remove('crazyit')
print(c_list)
c_list.clear()
print(c_list)