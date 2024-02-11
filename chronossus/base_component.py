class BaseComponent(object):

    @staticmethod
    def get_valid_values(limit) -> list:
        return list(range(*limit))

    def __init__(self,
                 name: str,
                 default_value: int = None,
                 limit: list = None,
                 if_limit: str = 'stop'):
        self.name = name
        self.default_value = default_value
        self.valid_values = self.get_valid_values(limit) if limit else None
        self.if_limit = if_limit

        self.marker = f'({self.name[0].upper()})'
        self.value = default_value

    def __repr__(self):
        return f'{self.marker}: {self.value}'

    def _is_valid(self, new_value):
        return new_value in self.valid_values

    def _get_value_if_valid(self, num) -> int:
        if self._is_valid(num):
            return num
        else:
            self._if_overage_func()
            return self.value

    def _change_value_by_num(self, num: int):
        n = -1 if num < 0 else +1
        for i in range(abs(num)):
            value = self._get_value_if_valid(self.value + n)
            self.value = value
        print('store', self.value)
        return self.value

    def _if_overage_func(self, stop=True):
        print(self.if_limit)
        if stop:
            raise StopIteration()
