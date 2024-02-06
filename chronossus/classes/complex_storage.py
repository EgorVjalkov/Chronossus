from random import randint, choice
from chronossus.classes.tokenstorage import TokenStorage


# нужно понять от чего он будет наследоваться
class TokenPool:
    def __init__(self,
                 pool_name: str,
                 default_tokens: dict,
                 limit: list,
                 if_limit: str = 'stop'):

        super().__init__(name=pool_name,
                         default_value=None,
                         limit=limit,
                         if_limit=if_limit)


@property
def token_num(self):
    if isinstance(self.value, list):
        return len(self.value)
    else:
        return self.value


def get_token_pool(self) -> list:
    token_pool = []
    for token_type in self.value:
        token_pool += [token_type] * self.value[token_type]
    self.value = token_pool
    return self.value


def remove_token_from_list(self, token):
    if token in self.value:
        self.value.remove(token)
    else:
        print('No token!')
    return self.value
def draw_tokens_from_pool(self,
                          draws: int) -> list:
    drawn = []
    for num in range(draws):
        if self.value:
            token = choice(self.value)
            result = self.change_value(-1, [token])
            if result is self.valid_values:
                return drawn
            else:
                drawn.append(token)
    return drawn



