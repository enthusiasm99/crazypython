scores = {'语文': 89}   #字典定义时，中间为冒号，切记！切记！切记！
print(scores)


scores['数学'] = 93
scores[92] = 5.7
print(scores)


del scores['语文']
del scores['数学']
print(scores)

cars = {'BMW' : 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars['BMW'] = 4.3
cars['AUDI'] = 3.5
print(cars)

print('AUDI' in cars)
print('PORSCHE' in cars)
print('LAMBORGHINI' not in cars)