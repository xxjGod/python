import os.path

alist = [0, 1, 2]
# assert isinstance(alist, list)
# assert isinstance(alist, dict)
print("xxk")


def demo_func(filename):
    if not os.path.isfile(filename):
        raise Exception


#demo_func("xxj")


def error_method():
    try:
        21 / 2
    except Exception as e:
        print(23)
        print("异常：\n" + str(e))
    finally:
        print("over")


error_method()
