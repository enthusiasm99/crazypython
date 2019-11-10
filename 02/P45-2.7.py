string = input("请输入原始字符串：")
i, chara = input("请输入想替换的位置及替换字符：").split()
position = int(i)
new_string = string[:position] + chara + string[position+1:]
print(new_string)