def gen_value(value: int,
              num: int,
              valid_values: list,
              recursion_flag: bool = False):
    v = value
    el = int(num / abs(num))
    for n in range(abs(num)):
        v += el
        if v not in valid_values:
            if recursion_flag:
                if el > 0:
                    yield min(valid_values)
                else:
                    yield max(valid_values)
            else:
                break
        else:
            value = v
            yield value


class BaseComponent(object):

    def __init__(self,
                 name: str,
                 value: int = None,
                 limit: int = None):
        self.name = name
        self.min = 0
        self.max = limit
        self.valid_values = list(range(self.min, self.max)) if limit else None

        self.marker = f'({self.name[0].upper()})'
        self.value = value
        self.recursion: bool = False

    def __repr__(self):
        return f'{self.marker}: {self.value}'

    def _is_valid(self, new_value):
        return new_value in self.valid_values

    def _change_value_by_num(self,
                             num: int):
        if num != 0:
            value_gen = gen_value(self.value, num, self.valid_values, recursion_flag=self.recursion)
            print('value', self.value)
            for i in range(abs(num)):
                self.value = next(value_gen)
                print('store', self.value)
        return self
