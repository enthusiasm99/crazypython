stack = []
stack.append('a')
print(stack)
stack.append('b')
print(stack)
stack.append('c')
print(stack)

# pop()方法：后入先出，将最后一次添加的元素移出栈，且该方法会返回出栈的元素
print(stack.pop())      # 输出 c
print(stack)            # ['a', 'b']
print(stack.pop())      # 输出 b
print(stack)            # ['a']