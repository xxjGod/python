import sys

from sqlalchemy.sql.functions import now


class Test:
    def test1(self, b):
        print(b, "x", 123)


# test = Test()
# me = test.test1
#
# me(12)
#
# print(type(None))
# str = '_handle_conflict_%s' % "123"
# print(str)
test = Test()
me = getattr(test, "test1")
print(me(12))


def _(param):
    pass


msg = _('invalid conflict_resolution value: %r')
print(sys.argv[1:])