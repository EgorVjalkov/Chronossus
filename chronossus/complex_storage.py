from random import choice
from base_component import BaseComponent


#def gen_list(token_pool, elements, valid_valies):
#    v = len(list)
#    el = int(rng / abs(rng))
#    for n in range(abs(rng)):
#        v += el
#        if v not in valid_values and el in :
#                break
#        else:
#            if el > 0:
#                list.append(element)
#            else:
#                list.remove(element)
#            yield list


class ComplexStorage(BaseComponent):

    @staticmethod
    def get_token_pool(tokens) -> list:
        if isinstance(tokens, dict):
            token_pool = []
            for token_type in tokens:
                token_pool += [token_type] * tokens[token_type]
            return token_pool
        else:
            return tokens

    def __init__(self,
                 pool_name: str,
                 tokens: dict | list,
                 limit: int,
                 die: list = None):

        super().__init__(name=pool_name,
                         value=0,
                         limit=limit)

        self.token_pool: list = self.get_token_pool(tokens)
        self.value = len(self.token_pool)
        self.die = die
        self.drawn: list = []

    def __repr__(self):
        return f"{self.name}: {self.token_pool}"

    @property
    def last_token(self):
        return self.token_pool[-1]

    def _change_token_pool_from_list(self,
                                     action: str,
                                     token_list: list) -> list:
        if action == 'add':
            self.token_pool.extend(token_list)
        else:
            for token in token_list:
                self.token_pool.remove(token)
        print('store', self.token_pool)
        return self.token_pool

    def _change_token_pool_by_die(self,
                                  action: str,
                                  rolls: int = 1) -> list:
        for r in range(rolls):
            token = choice(self.die)
            print('roll', token)
            self._change_token_pool_from_list(action, [token])
        return self.token_pool

    def _draw_tokens_from_pool(self,
                               draws: int) -> list:
        for num in range(draws):
            try:
                token = choice(self.token_pool)
            except IndexError:
                return self.drawn
            else:
                self._change_token_pool_from_list('rm', [token])
                self.drawn.append(token)
        return self.drawn

    def change_token_pool_by_(self,
                              die_rolls: int = None,
                              draws: int = None,
                              token_list: list = None,
                              action: str = None) -> list:
        try:
            if die_rolls:
                self._change_token_pool_by_die(action, die_rolls)
            elif draws:
                self._draw_tokens_from_pool(draws)
            else:
                self._change_token_pool_from_list(action, token_list)

        except ValueError:
            print('stop')
        return self.token_pool
