cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
print(cars.pop('AUDI'))    # 获取kye对应的value， 同时删除这个key-value对
print(cars)


cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
cars.popitem()  #  弹出（删除）创建cars{}时最后一个记录的key-value对
print(cars)

cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
k,v = cars.popitem()  # 删除创建cars{}时最后一个key-value对
print("%s -- %s" % (k, v))
print(cars)



