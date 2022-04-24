phones = ["Apple", "Huawei", "Xiaomi"]
for phone in phones:
    print("手机名：" + phone)

for index, phone in enumerate(phones):
    print(f"第{index + 1}把手机是{phone}")
    print("第{}把手机是{}".format(index + 1, phone))

for i in [0, 1, 2]:
    if i == 1:
        print(f"当前数是{i},将退出循环")
        break
    print("当前数是" + str(i))
else:
    print("正常结束break")

for i in [4, 5, 6]:
    if i == 5:
        print(f"当前数是{i},将退出循环")
        continue
    print("当前数是" + str(i))
else:
    print("正常结束continue")

age = 1
while age <= 3:
    if age == 2:
        break
    print(f"我{age}岁了")
    age += 1
else:
    print("可以上幼儿园了")

old_list = [0, 1, 2, 3, 4, 5]

# 普通遍历
# new_list = []
# for item in old_list:
#     if item % 2 == 0:
#         new_list.append(item)
new_list = [item * 2 for item in old_list if item % 2 == 0]

print(new_list)

old_student_score_info = {
    "Jack": {
        "chinese": 87,
        "math": 92,
        "english": 78
    },
    "Tom": {
        "chinese": 92,
        "math": 100,
        "english": 89
    }
}
# keys = [old_student_score_info[item] for item in old_student_score_info]
# print(keys)
# ir = (for scores in old_student_score_info.items())
# print(ir[0])
# new_student_score_info = {name: scores for name, scores in old_student_score_info.items() if scores["math"] == 100}


# inner = (item for item in keys[0])
# print(inner)
# print(item for item in inner)
# ir = ( for scores in old_student_score_info.items())
# print(ir)
new_student_score_info = {name: scores for name, scores in old_student_score_info.items() if scores["math"] == 100}
# print(new_student_score_info)

# for name, scores in old_student_score_info.items():
#     print(name)
#     print(scores)


old_list = [0, 0, 0, 1, 2, 3]
new_set = {item for item in old_list}
print(new_set)

new_list = (item for item in old_list)
print(type(new_list))

print("######################")

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print("")

print('\n'.join(
    [' '.join(['%2d *%2d = %2d' % (col, row, col * row) for col in range(1, row + 1)]) for row in range(1, 10)]))
