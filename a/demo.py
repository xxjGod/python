name = "Python编程时光"
print("导入成功")
print("__name__ 的值为: " + __name__)


def test():
    print("test123")


class Id:

    def __init__(self, id):
        self.id = id

    def id_name(self):
        print("id is:", self.id)


class Person(Id):

    def __init__(self, age, name, id):
        Id.__init__(self, id)
        self.age = age
        self.name = name

    def say(self):
        print(self.name)


class B:
    def __init__(self, b):
        print(b)
        print("B")


class C:

    def test(self):
        print(123)


class A(C, B):
    def __init__(self):
        m = super(A, self).__init__
        m(5)


class D:
    def test(self):
        print(123)


class E(object):
    def test(self):
        print(123, "xxj")
