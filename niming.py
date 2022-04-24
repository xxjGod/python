from functools import reduce
from typing import Iterator


def mySUm(x, y):
    return x + y


print(mySUm(2, 3))
print((lambda x, y: x + y)(2, 4))
print((lambda x, y: x if x < y else y)(1, 2))
fuc = lambda n: 1 if n == 0 else n * fuc(n - 1)
print(fuc(5))

c = map(lambda x: x * 2, [1, 2, 3, 4, 5])
# for key, val in c.items():
#     print(key)
#     print(val)
print(isinstance(c, Iterator))
print(next(c))
for item in range(-5, 5):
    print(item)

itema = [item for item in range(-5, 5)]
print(itema)

f = filter(lambda x: x < 0, range(-5, 5))
print(type(f))
print(isinstance(f, Iterator))
print(type(Iterator))

# m = {"xxj": 10}
# print(m["xxj"])
# print(type(m))

re = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(re)

key = lambda x: len(x)
print(key("12"))

print((lambda x: len(x))("2341"))
