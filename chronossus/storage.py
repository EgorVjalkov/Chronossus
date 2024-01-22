from random import randint, choice


class TokenStorage:
    def __init__(self,
                 storage_name: str,
                 default_tokens: int | dict,
                 default_token_num: int,
                 limit: list,
                 if_limit: str = 'stop',
                 die: list = None):

        self.token_name = storage_name
        self.default_tokens_num = default_token_num
        self.limit = limit
        self.die = die
        self.if_limit = if_limit

        self.tokens = default_tokens
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

    def is_overage(self, result):
        token_num = list(range(*self.limit))
        return result not in token_num

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

    def add_tokens_by_die(self,
                          rolls: int = 1) -> int | str:
        for num in range(rolls):
            add_tokens = choice(self.die)
            print(add_tokens)
            if self.is_overage(self.token_num+add_tokens):
                return self.if_limit
            else:
                self.tokens += add_tokens
        return self.tokens

    def add_tokens_by_num(self,
                          token_num: int,
                          token_list: list = None):

        for token in range(token_num):
            if self.is_overage(self.token_num+1):
                return self.if_limit
            else:
                if token_list:
                    self.token_pool.append(token_list.pop(token_list.index(token)))
                else:
                    self.tokens += 1
        return self

    def add_(self,
             mod: str = 'simple',
             token_num: int = None,
             token_list: list = None,
             rolls: int = None) -> object:

        if mod == 'by_die':
            return self.add_tokens_by_die(rolls)
        else:
            return self.add_tokens_by_num(token_num, token_list)

    def spend_(self, tokens: int | list):
        if self.token_pool:
            for token in tokens:
                self.token_pool.remove(token)
            return self.token_pool
        else:
            self.tokens -= tokens
            return self.tokens


ts = TokenStorage('EnergyPool',
                  {'ch': 5, 'ex': 5},
                  10,
                  limit=[0, 20],
                  if_limit='stop')
ts.get_token_pool()
print(ts)
# автоматизируй работу с жетонами. сделай функции спенд и адд в одной, возиожно так можно.
# нужно сделать токенс универвльной переменной чтоб не париться с токенс пулом
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
                       0,
                       limit=[0, 3],
                       if_limit='anomaly',
                       die=[0, 1, 1, 1, 1, 2])
print(paradox)
overage = paradox.add_(token_num=3)
#overage = paradox.add_(mod='by_die', rolls=3)
print(paradox)
print(overage)
#paradox.spend_(1)
#print(paradox)
