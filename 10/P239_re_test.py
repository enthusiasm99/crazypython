import re
pa = re.compile('fkit')
print(pa.match('www.fkit.org', 4).span())
print(pa.match('www.fkit.org', 4))
print(pa.match('www.fkit.org', 4, 6))
print(pa.fullmatch('www.fkit.org', 4, 8).span())
print(pa.fullmatch('www.fkit.org', 4, 8))