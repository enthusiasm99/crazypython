a = 5
b = 3
st = 'a大于b' if  a > b  else 'a小于b'
# print(st)


st2 = print('crazyit') if  a > b  else 'a小于b'
print(st2)

for i in range(10):
    print(i)

for j in range(10):
    print(j, end = "")

print(1)
print("")
print(2)
print(3)

a=[""]
a[0] = 'aa'
a[1] = 'bb'
for i in range(2):
    #print(i)
    print(a[i])
    print("")


class Dog:
    #abc = 1
    def abc(self):
        print('我是来测试的')

d = Dog()
print(d.abc())