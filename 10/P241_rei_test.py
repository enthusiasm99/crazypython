import re
m = re.findall(r'fkit', "Fkit is a good domain, FKIT is good")
print(m)

print('------------华丽的分割线-----------')

m2 = re.findall(r'fkit', "Fkit is a good domain, FKIT is good", re.I)
print(m2)