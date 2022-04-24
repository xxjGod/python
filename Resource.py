class Resource():
    def __enter__(self):
        print("==begin==")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("==end==")
        print(exc_type)
        return True

    def operate(self):
        print("==operate==")
        1/0


with Resource() as res:
    res.operate()
