s = 'crazyit.org is very good'

print(s[2])           # a
print(s[-4])          # g
print(s[3:5])         # zy
print(s[3:-5])        # zyit.org is very
print(s[::-1])        # 第3个参数（step），-1可实现逆序打印 doog yrev si gro.tiyzarc
print(s[5:])          # it.org is very good
print(s[-6:])         # y good
print(s[:5])          # crazy

print('is' in s)           # True
print("love" in s)         # False

print(len(s))              # 24
print(len("i love you"))   # 10

print(max(s))           # z
print(min(s))           # 空格