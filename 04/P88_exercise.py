#先在草稿本上画图，标明行列编号，通过数字走向、行列编号数字变化查找规律

num = int(input("请输入一个给定的数字："))

array = [[0] * num]
for i in range(1, num):
    array += [[0] * num]

'''
orient代表方向, 按照走向，最开始为向下的
0：向下，也就是列不变，行+1
1：向右，也就是行不变，列+1
2：向左，也就是行不变，列-1
3：向上，也就是列不变，行-1
'''
orient = 0
j = 0
k = 0

for i in range(1, num * num + 1):
    array[j][k] = i    #从1到给定数字的平方，通过行列编号的变化挨个赋值

#通过数字走向、行列编号数字变化查找规律
    if( j + k == num -1):
        if(j > k):
            orient = 1
        else :
            orient = 2
    elif(j ==k) and (k >= num / 2):
        orient = 3
    elif(j == k -1 ) and (k <= num/2):
        orient = 0

#找到4根线后，行列编号数字变化的规律
    if(orient == 0):
        j += 1
    elif(orient == 1):
        k += 1
    elif(orient == 2):
        k -= 1
    elif(orient == 3):
        j -= 1

for x in range(num):
    for y in range(num):
        # 注意"%02d "， 双引号中有个空格，print自动以换行结尾，使用end不换行
        print("%02d " % array[x][y], end="")
    print("")  #在print完一行后，启换行作用

