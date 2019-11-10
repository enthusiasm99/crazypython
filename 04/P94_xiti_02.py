size = int(input("请输入一个数字："))

for i in range(1, size + 1):
    # 空格与行数i的关系
    kongge = " " * (size - i)
    # *与行数i的关系
    stars = "*" * (2 * i - 1)
    print(kongge + stars)