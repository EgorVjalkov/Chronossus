from random import randint, choice


class TokenStorage:
    def __init__(self, storage_name: str, tokens: int | dict):
        self.token_name = storage_name
        self.tokens = tokens
        self.token_pool = []

    def __repr__(self):
        if self.token_pool:
            return f'TokenStorage "{self.token_name}": {self.token_pool}'
        else:
            return f'TokenStorage "{self.token_name}": {self.tokens}'

    @property
    def token_num(self):
        if self.token_pool:
            return len(self.token_pool)
        else:
            return self.tokens

    def get_token_pool(self) -> list:
        for token_type in self.tokens:
            self.token_pool += [token_type] * self.tokens[token_type]
        return self.token_pool

    def draw_from_pool(self, tokens: int) -> list:
        drawn = []
        for num in range(tokens):
            last_token_index = len(self.token_pool) - 1
            token = self.token_pool.pop(randint(0, last_token_index))
            drawn.append(token)
        return drawn

    def add_(self, tokens: int | list,
             mod: str = 'simple',
             rolls: int = 0) -> object:

        if mod == 'by_die':
            for num in range(rolls):
                self.tokens += choice(tokens)
        else:
            if isinstance(tokens, list):
                self.token_pool.extend(tokens)
            else:
                self.tokens += tokens
        return self

    def spend_(self, tokens: int | list):
        if self.token_pool:
            for token in tokens:
                self.token_pool.remove(token)
        else:
            self.tokens -= tokens
        return self
    #@classmethod
    #def get_e_pack_tokens_in_new_era(cls):
    #    cls.get_token_pool()
    #    cls.


ts = TokenStorage('EnergyPool', {'ch': 5, 'ex': 5})
ts.get_token_pool()
print(ts)
drawn = ts.draw_from_pool(tokens=3)
print(drawn)
print(ts)
ts.add_(['ex'])
print(ts)

vp = TokenStorage('VPs', 0)
print(vp)
vp.add_(2)
print(vp)
vp.spend_(2)
print(vp)

paradox = TokenStorage('ParadoxStorage', 0)
print(paradox)
paradox.add_([0, 1, 1, 1, 1, 2], mod='by_die', rolls=1)
print(paradox)
paradox.spend_(1)
print(paradox)
