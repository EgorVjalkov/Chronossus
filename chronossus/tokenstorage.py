from random import choice
from base_component import BaseComponent


class TokenStorage(BaseComponent):
    def __init__(self,
                 storage_name: str,
                 default_token_num: int,
                 limit: list = None,
                 if_limit: str = 'stop',
                 die: list = None):

        super().__init__(name=storage_name,
                         default_value=default_token_num,
                         limit=limit,
                         if_limit=if_limit)

        self.die = die

    def _change_value_by_die(self,
                             rolls: int) -> int:
        for r in range(rolls):
            token_num = choice(self.die)
            print('roll', token_num)
            self._change_value_by_num(token_num)
        return self.value

    def change_value_by_(self,
                         num: int = None,
                         die: bool = False,
                         rolls: int = None):
        try:
            if die:
                self._change_value_by_die(rolls)
            else:
                self._change_value_by_num(num)
        except StopIteration:
            return self.value
        return self.value
