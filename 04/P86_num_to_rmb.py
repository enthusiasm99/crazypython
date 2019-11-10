'''
  总思路：
  1、将浮点数分成整数部分、小数部分
  2、整数部分，按每4位数进行划分，因为中文读法为四位数字循环，再加亿、万
  3、小数部分，乘100取整，四舍五入，保留两位。
'''

# 转为整数、小数的函数，注意小数
def divide(num):
    integer = int(num)
    fraction = round((num - integer) * 100)  # 注意round的用法
    return (str(integer), str(fraction))

# 整数4位数的读法，不考虑 亿、万
han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
unit_list = ["拾", "佰", "仟"]

def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    for i in range(num_len):
        num = int(num_str[i])
        # 不是最后一位数字，且不是零，则要添加单位（拾, 佰, 仟）
        if i != num_len -1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不要添加单位（拾, 佰, 仟）
        else :
            result += han_list[num]
    # 上述循环后，result会出现多个带零的情况，穷举带“零”的特殊情况，找规律
    if ("零零零" in result):
        result = result.replace("零零零", '') # 更换前，1000转换为：壹仟零零零
    elif("佰零零" in result):
        result = result.replace("佰零零", '佰') # 更换前，1200转换为：壹仟贰佰零零
    elif("拾零" in result):
        result = result.replace("拾零", '拾') # 更换前，1020转换为：壹仟零贰拾零
    elif ("仟零零" in result):
        result = result.replace("仟零零", '仟零') # 更换前，1004转换为：壹仟零零肆
    return result

def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12 :
        print("数字太大，翻译不了！")
        return
    #如果大于8位，包含单位“亿”、“万”，注意序号
    elif str_len >8 :
        return four_to_hanstr(num_str[:-8]) + "亿" + \
               four_to_hanstr(num_str[-8:-4]) + "万"  + \
               four_to_hanstr(num_str[-4:]) + "圆"
    # 如果大于8位，包含单位“万”
    elif str_len >4 :
        return  four_to_hanstr(num_str[-8:-4]) + "万" + \
               four_to_hanstr(num_str[-4:]) + "圆"
    else :
        return four_to_hanstr(num_str) + "圆"

def fraction_to_str(num_str):
    #若长度为2的情况
    if len(num_str) == 2:
        num1 = int(num_str[0])
        num2 = int(num_str[1])
        if num2 == 0:
            result = han_list[num1] + "角"
        else :
            result = han_list[num1] + "角" + han_list[num2] + "分"
    elif len(num_str) == 1:
        num3 = int(num_str[0])
        if num3 == 0:
            result = ""
        else:
            result = han_list[num3] + "分"
    return result


num = float(input("请输入一个小数："))
integer, fraction = divide(num)
print(fraction)
print(integer_to_str(integer) + fraction_to_str(fraction))

