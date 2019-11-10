class User():
    def walk(self):
        print(self, "正在慢慢地走")

# User.walk()

u = User()
User.walk(u)  # <__main__.User object at 0x000000000262EEB8> 正在慢慢地走

User.walk("fkit")   # fkit 正在慢慢地走