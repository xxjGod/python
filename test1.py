def test(a: int, b: str) -> str:
    print(a, b)
    return 1000


if __name__ == '__main__':
    print(type(test('test', 'abc')))
