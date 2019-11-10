# 创建一个空的bytes
b1 = bytes()
print("b1是：", b1)

# 创建一个空的bytes值
b2 = b''
print("b2是：", b1)
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'

print("b3是：",b3)
print("b3-2是：",b3[0])
print("b3-3是：",b3[2:4])

# 调用bytes()方法将字符串转换成bytes对象
b4 = bytes('我爱Python编程！', encoding = 'utf-8')
print("b4是：",b4)
# 利用字符串的encode()方法编码成bytes
b5 = "学习Python很有趣".encode(encoding = 'utf-8')
print("b5是：",b5)
