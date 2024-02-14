from random import choice
from base_component import BaseComponent


class ComplexStorage(BaseComponent):

    @staticmethod
    def get_token_pool(default_tokens) -> list:
        token_pool = []
        for token_type in default_tokens:
            token_pool += [token_type] * default_tokens[token_type]
        return token_pool

    def __init__(self,
                 pool_name: str,
                 default_tokens: dict,
                 limit: list,
                 if_limit: str = 'stop',
                 die: list = None):

        super().__init__(name=pool_name,
                         default_value=0,
                         limit=limit,
                         if_limit=if_limit)

        self.token_pool: list = self.get_token_pool(default_tokens)
        self.value = len(self.token_pool)
        self.die = die
        self.drawn: list = []

    @property
    def last_token(self):
        return self.token_pool[-1]

    def _change_token_pool_decorator(self, new_value):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if new_value != self.value:
                    try:
                        return func(*args, **kwargs)
                    except ValueError:
                        self._if_overage_func()

            return wrapper

        return decorator

    def _try_to_change_token_pool(self, action, token):
        if action == 'add':
            new_value = self._set_value_if_valid(self.value + 1)

            @self._change_token_pool_decorator(new_value)
            def append_token(token_name):
                self.token_pool.append(token_name)
                self.value = new_value
                return self.token_pool

            return append_token(token)

        else:
            new_value = self._set_value_if_valid(self.value - 1)

            @self._change_token_pool_decorator(new_value)
            def remove_token(token_name):
                self.token_pool.remove(token_name)
                self.value = new_value
                return self.token_pool

            return remove_token(token)

    def _change_token_pool_from_list(self,
                                     action: str,
                                     token_list: list) -> list:
        for token in token_list:
            self._try_to_change_token_pool(action, token)
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
                self._if_overage_func()
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

        except StopIteration:
            return self.token_pool
