from collections.abc import Iterator


class Array:
    index = 0
    mylist = [0, 1, 2]

    def _iter_(self):
        return self

    def __next__(self):
        if self.index <= len(self.mylist) - 1:
            value = self.mylist[self.index]
            self.index += 1
            return value
        raise StopIteration

    def generator_factory(top=5):
        index = 0
        while index < top:
            print("index 值：" + str(index))
            index += 1
            yield index
        raise StopIteration





gen=generator_factory()
gen

my_iterator = iter(Array())
print(isinstance(my_iterator, Iterator))
print(next(my_iterator))
