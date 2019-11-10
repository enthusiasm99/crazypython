cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
cars.clear()
print(cars)


cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.get('BMW'))
print(cars.get('POSCHE'))   # None
print(cars['POSCHE'])       # KeyError: 'POSCHE'

cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars.update({'BMW': 4.5, 'POSCHE':12})          # 找到key值，则修改； 未找到，则增加
print(cars)



cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
ims = cars.items()
print(type(ims))
print(list(ims))      # 需要与list()结合使用
print(list(ims)[1])

kys = cars.keys()
print(type(kys))
print(list(kys))      # 需要与list()结合使用
print(list(kys)[0])

vals = cars.values()
print(type(vals))
print(list(vals))      # 需要与list()结合使用
print(list(vals)[0])
