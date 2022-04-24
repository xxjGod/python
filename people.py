print(__name__)
print(__file__)


def __init__(self):
    print(self)


__init__("name")

list1 = [1, 2, 3, 3, 4]
s1 = set(list1)
print(s1)

dws = {}
# print(dws.empty)
print(type(dws))
print(dws is not None)
print(int(7.8))


def test1(b, a=3):
    print(b)


test1(b=2, a=4)
test1(4)
if not False:
    print("123")

map4 = {"name": "xxj", "age": 18}
print(type(map4.values()))
print(list(map4.values()))

SUBJECT_MAP = {
    201: ("chinese", 6369),
    202: ("math", 499),
    203: ("english", 18858),
    204: ("physics", 10449),
    205: ("chemistry", 12358),
}

print(SUBJECT_MAP.values())

for item in SUBJECT_MAP.values():
    print(item[0])

tuple1 = (1, 2, 3, 6)
print(tuple1[0])

list1 = [(1, 2, 3), (7, 8, 9)]
for _, b, c in list1:
    print(f"{_}lala{b}lala{c}")
