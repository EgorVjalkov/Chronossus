from random import randint, choice


def if_limit_decorator(func):
    def wrapper(*args, **kwargs):
        result: TokenStorage = func(*args, **kwargs)
        if result.token_num <= result.limit:
            return result
        else:
            print(f'стоп-слово: {result.if_limit}')
        return wrapper()


class TokenStorage:
    def __init__(self,
                 storage_name: str,
                 tokens: int | dict,
                 limit: int,
                 if_limit: str = 'stop',
                 die: list = None):

        self.token_name = storage_name
        self.tokens = tokens
        self.limit = limit
        self.die = die
        self.if_limit = if_limit

        self.token_pool = []

    def __repr__(self):
        if self.token_pool:
            return f'TokenStorage "{self.token_name}": {self.token_pool}'
        else:
            return f'TokenStorage "{self.token_name}": {self.tokens}'

    def get_token_pool(self) -> list:
        for token_type in self.tokens:
            self.token_pool += [token_type] * self.tokens[token_type]
        return self.token_pool

    @property
    def token_num(self):
        if self.token_pool:
            return len(self.token_pool)
        else:
            return self.tokens

    @if_limit_decorator
    def draw_from_pool(self, tokens: int) -> list:
        drawn = []
        for num in range(tokens):
            last_token_index = len(self.token_pool) - 1
            token = self.token_pool.pop(randint(0, last_token_index))
            drawn.append(token)
        return drawn

    @if_limit_decorator
    def add_(self,
             mod: str = 'simple',
             tokens: int | list = None,
             rolls: int = None) -> object:

        if mod == 'by_die':
            for num in range(rolls):
                self.tokens += choice(self.die)
                print(self.token_num)
        else:
            if isinstance(tokens, list):
                self.token_pool.extend(tokens)
            else:
                self.tokens += tokens
        return self

    @if_limit_decorator
    def spend_(self, tokens: int | list):
        if self.token_pool:
            for token in tokens:
                self.token_pool.remove(token)
        else:
            self.tokens -= tokens
        return self


#ts = TokenStorage('EnergyPool', {'ch': 5, 'ex': 5}, 0)
#ts.get_token_pool()
#print(ts)
#drawn_t = ts.draw_from_pool(tokens=3)
#print(drawn_t)
#print(ts)
#ts.add_(tokens=['ex'])
#print(ts)
#
#vp = TokenStorage('VPs', 0)
#print(vp)
#vp.add_(tokens=2)
#print(vp)
#vp.spend_(2)
#print(vp)

paradox = TokenStorage('ParadoxStorage',
                       0,
                       limit=3,
                       if_limit='anomaly',
                       die=[0, 1, 1, 1, 1, 2])
print(paradox)
print(type(paradox))
paradox.add_(mod='by_die', rolls=3)
print(paradox)
paradox.spend_(1)
print(paradox)
