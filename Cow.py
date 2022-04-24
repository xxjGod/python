from dataclasses import dataclass


@dataclass
class CowDemo:
    age: int
    name: str


    def eat(self):
        print(self.name, self.age)


cow = CowDemo()
cow.eat()
