class Bird:
    age = 18

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(type(self), id(self))
        print(f"{self.name}开始吃饭")

    @staticmethod
    def run():
        print("飞")

    @classmethod
    def sleep(cls):
        print("睡觉", id(cls))

    @classmethod
    def sleep2(cls):
        print(type(cls), cls.age, Bird.__dict__)
        print("睡觉2", id(cls))


# 普通方法
b1 = Bird("黄鹂")
b1.eat()
Bird.sleep2()
# b2 = Bird("鹦鹉")
# Bird.eat(b2)
# # 静态方法
# b1.run()
# Bird.run()

# 类方法
# b2.sleep()
# Bird.sleep2()
# claz = {}
# print(id(Bird))
# claz["xxj"] = Bird
# msg = claz.setdefault("xxj", {})
# print(id(msg))
# print(id(claz["xxj"]))
# print("***********")
# print(Bird.objects)

map1 = {'name': 'xxj', 'age': 18}

print(type(map1))
print(**map1)
