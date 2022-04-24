dic = {'name': 'xxj', 'age': 18}
print(dic['name'])
dic['color'] = 'red'
print(dic.get('sex', 1))
print(len(dic))
# del dic['name']
print(len(dic))
print(dic)

print("########key##########")
for key in dic.keys():
    print(key)

print("########item##########")
for key, _ in dic.items():
    print(key)
    print(_)
print("########value##########")
for vl in dic.values():
    print(vl)
if 'sex' not in dic.keys():
    print("不包含sex")

for key in sorted(dic.keys()):
    print(key)


