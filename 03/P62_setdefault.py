cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.setdefault('POSCHE', 20))      #中间为逗号， 字典中没有，则输出给定的VALUE默认值
print(cars.setdefault('BMW', 10))         #有，则输出字典中对应的VALUE

a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)

b_dict = dict.fromkeys((13, 17))
print(b_dict)

c_dict =  dict.fromkeys([13, 17], 'good')
print(c_dict)     # 指定默认的value值