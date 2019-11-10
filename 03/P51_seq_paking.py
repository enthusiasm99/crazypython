vals = 10, 20, 30
print(vals)
print(type(vals))

a_tuple = tuple(range(1, 10, 2))   #注意右侧的tuple()方法
print(a_tuple)
print(type(a_tuple))
a, b, c, d, e = a_tuple
print(a, b, c, d, e)

a_list = ['fkit', 'crazyit']
a_str, b_str = a_list
print(a_str, b_str)


x, y, z = 10, 20, 30
print(x, y, z)

x, y, z = y, z, x
print(x, y, z)


first, second, *rest = range(10)   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(first)   # 0
print(second)  # 1
print(rest)    # [2, 3, 4, 5, 6, 7, 8, 9]

*begin, last = range(1,10)   #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(begin) # [1, 2, 3, 4, 5, 6, 7, 8]
print(last)  #9

num1, *num_mid, num_last = range(2,10)   #[2, 3, 4, 5, 6, 7, 8, 9]
print(num1)     # 2
print(num_mid)  # [3, 4, 5, 6, 7, 8]
print(num_last) # 9

