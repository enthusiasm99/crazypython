a_list = ['crazyit', 20, -1.2]
a_list.append('fkit')
print(a_list)

a_tuple = (3.4, 5.6)
a_list.append(a_tuple)
print(a_list)

a_list.append(['a', 'b'])
print(a_list)


b_list = ['a', 30]
b_list.extend([-2, 3.1])
print(b_list)
b_list.extend(['C', 'R', 'A'])
print(b_list)
b_list.extend(range(97,100))
print(b_list)

c_list = list(range(1,6))
print(c_list)
c_list.insert(3, 'crazyit')
print(c_list)
c_list.insert(3, tuple('crazy'))    # tuple('crazy') 结果： ('c', 'r', 'a', 'z', 'y')
print(c_list)