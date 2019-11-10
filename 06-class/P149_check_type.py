hello = 'Hello'
print(isinstance(hello, str))
print(isinstance(hello, object))
print(issubclass(str, object))

data = (20, 'fkit')
print(isinstance(data, (list, tuple)))

print(issubclass(str, (list, tuple)))

print(issubclass(str, (list, tuple, object)))