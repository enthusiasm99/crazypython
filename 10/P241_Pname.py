import re
m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)', r"www.fkit.org is a good domain")
print(m2)
print(m2.groupdict())

m3 = re.search(r'fkit.org', r"www.fkit.org is a good domain")
print(m3)
print(m3.groupdict())