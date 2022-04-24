from functools import partial


#
# def power(x, n):
#     s = 1
#     while n > 0:
#         n -= 1
#         s = s * x
#     return s
#
#
# print(power(3, 2))
#
# power_2 = partial(power, n=2)
# print(power_2(3))


def deco():
    age = 10

    def wrapper():
        nonlocal age
        age += 1
        print(age)

    return wrapper


deco()()

# def test1():
#     global xtest
#     xtest = 19
bak = "xxj"


def foo1():
    print("i am a func")


def bar():
    foo = "i am a string"
    foo_dup = globals().get("foo1")
    print(foo_dup)


bar()

other = "test"


def foobar():
    name = "xxj"
    gender = "male"
    for key, vaule in locals().items():
        print(key, "=", vaule)


foobar()
