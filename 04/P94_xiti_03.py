# 规律为“定1的起始位置（均相同），上向右上”。 详见“F:\IT Study\Python\005-买书-源码\20190721-疯狂Python讲义\P94_xiti_03_横竖斜的总和相同示意图.xlsx”
# 若右上为零（即没有赋值），则往右上走，否则往下走，再往右上走
# 注意几个特殊位置：最上行、最右列、右上角
# 开始时，发现结果不对：
#   1、少了一个右上角的特殊情况；
#   2、少了第28行i的限制条件。后发现每个if（elif）均有i、j共2个判断条件，唯有28行只有一个j条件，但输出结果不正确，与其它if一样加上缺失的i条件后，则正确了

num = int(input("请输入一个给定的数字："))

array = [[0] * num]
for i in range(1, num):
    array += [[0] * num]

i = 0
# 定位1的起始位置，为固定的
j = int((num - 1) / 2)

for x in range(1, num * num + 1):
    array[i][j] = x
    # 处理第一排的情况
    if(i == 0 and j != num -1):
        i = num -1
        j += 1
    # 处理右上角的情况
    elif (i == 0 and j == num - 1):
        i += 1
    # 处理最右列的情况
    elif(i != 0 and j == num -1):  #注意i的限制条件，不加的话，可能与上一个条件中的i条件重复
        i -= 1
        j = 0
    # 不是以上特殊位置的时候
    elif(i != 0 and j != num -1):
        #判断右上是否有其它的数， 若有，则往下走一格。
        if(array[i-1][j+1] > 0):
            i += 1
        #若没有，则往右上走一格
        else:
            i -= 1
            j += 1

for x in range(num):
    for y in range(num):
        # 注意"%03d "， 双引号中有个空格，print自动以换行结尾，使用end不换行
        print("%03d " % array[x][y], end="")
    print("")  #在print完一行后，启换行作用




