# 使用temp来指定输出格式
temp = '书名是: %(name)s, 价格是: %(price)010.2f, 出版社是: %(publish)s'
books = {'name': '疯狂Python讲义', 'price': 78.9, 'publish': '电子社'}
print(temp % books)

books = {'name': '疯狂JAVA讲义', 'price': 88.5, 'publish': '电子社'}
print(temp % books)