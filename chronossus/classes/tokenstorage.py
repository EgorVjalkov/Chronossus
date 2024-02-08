from random import randint, choice
from chronossus.classes.base_component import BaseComponent


class TokenStorage(BaseComponent):
    def __init__(self,
                 storage_name: str,
                 default_token_num: int,
                 limit: list,
                 if_limit: str = 'stop',
                 die: list = None):

        super().__init__(name=storage_name,
                         default_value=default_token_num,
                         limit=limit,
                         if_limit=if_limit)

        self.die = die

    def _change_token_num(self, tokens: int):
        n = -1 if tokens < 0 else +1
        for i in range(abs(tokens)):
            value = self.get_value_if_valid(self.value + n) # <-- break?
            self.value = value
        print('store', self.value)
        return self.value

    def _change_token_num_by_die(self,
                                rolls: int) -> int:
        for r in range(rolls):
            token_num = choice(self.die)
            print('roll', token_num)
            self._change_token_num(token_num)
        return self.value

    def change_token_num_by_(self,
                             num: int = None,
                             die: bool = False,
                             rolls: int = None):
        try:
            if die:
                self._change_token_num_by_die(rolls)
            else:
                self._change_token_num(num)
        except StopIteration:
            return self.value
        return self.value

