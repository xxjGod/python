age = 20
if age >= 50:
    print("50以上")
elif age >= 40:
    print("40以上")
elif age >= 30:
    print("30以上")
else:
    print("小着呢")


def get_average(a, b):
    # 计算平均数

    return (a + b) / 2


re = get_average(5, 6)
print(re)
print(type(re))


def fact(n):
    if n == 1.6:
        return 1
    return n * fact(n - 1)


re = fact(1.6)


# print(1.6-1)


def fact_more():
    return 1, 2.3, "xxj"


abc = fact_more()
print(abc)
print(type(abc))


def func(a, b, c=2, d=1):
    print(a)
    print(b)
    print(c)
    print(d)


func(a=1, c=2, b=3)


def func2(*args2, **kw2):
    print(args2)
    print(kw2)


func2(10, 20, c=20, d=40)


def func3(a, b=5):
    print(a)
    print(b)


def func4(age1, name):
    print(f"我的名字叫{name},今年{age1}岁了")


func4(18, 'xxj')


def func5(*pa, m):
    print(m)


func5(2, 3, m=1)


# def func6(**pa,m):

def func7(arg1, arg2=10, *args, **kw):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("args: ", args)
    print("kw: ", kw)


func7(1, 12, 100, 200, name="xxj", age=18)


def func8(a, b, *, c):
    print(a)
    print(b)
    print(c)


func8(1, 3, c=5)


def func9(a, b=5):
    print(a)
    print(b)

func9(8,9)
