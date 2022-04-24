# name = input("请输入姓名：")
# print('哦原来是：' + name)
#
# age = input("请输入年龄：")
# if int(age) >= 18:
#     print("成人")
# else:
#     print("未成年")
while True:
    chargNum = input("请输入数字：")
    if chargNum == '结束':
        break

    if int(chargNum) % 2 == 0:
        print("偶数")
    else:
        print("奇数")

print("结束程序")
