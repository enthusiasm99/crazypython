a_list = [2, 4, -3.4, 'crazyit', 23]
print(a_list)
a_list[2] = 'fkit'
print(a_list)
a_list[-2] = 9527
print(a_list)


b_list = list(range(1, 5))
print(b_list)
b_list[1: 3] = ['a', 'b']      #个数相同，直接替换
print(b_list)                  #[1, 'a', 'b', 4]

b_list[2: 2] = ['x', 'y']      #个数不相同，不为空，则插入
print(b_list)                  #[1, 'a', 'x', 'y', 'b', 4]

b_list[2: 4] = []             #个数不相同，为空，则删除
print(b_list)                 #[1, 'a', 'b', 4]

b_list[2: 3] = []       #个数相同，直接替换
print(b_list)           #[1, 'a', 4]

# 'Charlie' 不会作为一个整体，每个字符都是一个元素
#注意，原列表中只保存了1，  'a', 4  被替换了
b_list[1: 3] = 'Charlie'
print(b_list)               #[1, 'C', 'h', 'a', 'r', 'l', 'i', 'e']

#若以上语句为下面的，结果不一样，只有 'a'被替换，4保留
b_list[1: 2] = 'Charlie'
print(b_list)               #[1, 'C', 'h', 'a', 'r', 'l', 'i', 'e', 4]

c_list = list(range(1, 10))
print(c_list)
#若指定了步长，则需要左右两边的个数相同
c_list[2: 9: 2] = ['a', 'b', 'c', 'd']
print(c_list)