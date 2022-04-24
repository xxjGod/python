import os


class Animal:

    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name}跑起来了")


dog = Animal(name="小黑")
print(dog.name)
dog.run()

dog2 = Animal(name="小2")
Animal.run(dog2)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(BASE_DIR)


def F(**a):
    print(a)


dt = {"xxj": 21}


F(xxj=18,age=14)
print(not dt)
set2={1,3,4,5}
#print(set2.skip(2))

for i in range(4):
    print(i)
