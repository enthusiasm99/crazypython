a_list = list(range(1, 10))
print(a_list)       #[1, 2, 3, 4, 5, 6, 7, 8, 9]
a_list.reverse()
print(a_list)       #[9, 8, 7, 6, 5, 4, 3, 2, 1]

b_list = [3, 4, -2, -30, 14, 9.3, 3.4]
print(b_list)
b_list.sort()
print(b_list)       # ['Erlang', 'Go', 'Kotlin', 'Python', 'Rubby', 'Swift']

c_list = ['Python', 'Swift', 'Rubby', 'Go', 'Kotlin', 'Erlang']
c_list.sort()
print(c_list)

c_list.sort(key=len)  #按长度排序
print(c_list)           # ['Go', 'Rubby', 'Swift', 'Erlang', 'Kotlin', 'Python']
c_list.sort(key=len, reverse=True)
print(c_list)           # ['Erlang', 'Kotlin', 'Python', 'Rubby', 'Swift', 'Go']