# import argparse
#
# parser = argparse.ArgumentParser(description='test')
#
# parser.add_argument('--sparse', action='store_true', default=False, dest='sq', help='GAT with sparse version or not.')
# parser.add_argument('--seed', type=int, default=72, help='Random seed.')
# parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')
#
# args = parser.parse_args()
# print(type(args.sq))
# print(args.seed)
# print(args.epochs)
#
# mpvalue = {"age": 18}
# mp = {"xxj": mpvalue}
#
# print(mp["xxj"]["age"])
#
# mpq1 = {"name": "xxj", "age": 18}
# mpq2 = {"name": "xxr", "age": 20}
# lst = [mpq1, mpq2]
# lst2 = []
# for item in lst:
#     if "name2" in item:
#         print(item["name2"])
#

# map1 = {'name': 'xxj', 'age': 21}
# map1.dict()
# list1 = [['a', 'b', 'c'], [1, 2]]
#
# result = [it for item in list1 for it in item]
# print(result)
# str = 'helloworld'
#
# e = enumerate(str)
# for index,item in e:
#     print(index,item)

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
#
#
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(g.send(7))

#msg =%(qid)s
