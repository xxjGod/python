class Demo:
    def __init__(self):
        self.foo = 11
        self._bar = 22
        self.__baz = 33
        self.__session_factory_map = {}

    def test1(self, ss: int = 3):
        self.__session_factory_map = {"xxj": 12}


demo1 = Demo()

print(demo1.foo)
print(demo1._bar)
print(dir(demo1))
print(demo1._Demo__session_factory_map)
demo1.test1("5")
print(demo1._Demo__session_factory_map)

book_tag_sql = """
      select tt.f_textbook_id, tt.f_tag_id, ti.f_type, ti.f_sort_index, ti.f_weight
      from t_textbook_tag as tt left join t_tag_info as ti
      on tt.f_tag_id = ti.f_id
      where
          tt.f_textbook_id = :book_id
          and ti.f_type in ("knowledge", "test_method", "solution")
          and ti.f_valid = 1
      """
print(type(book_tag_sql))

kp = {"knowledge_points1": [1]}

ws = kp.get("knowledge_points", [22]) if kp else [2, 3]

print(ws)
