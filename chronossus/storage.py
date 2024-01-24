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
        self.limit = list(range(*limit))
        self.die = die
        self.if_limit = if_limit

        self.tokens = default_tokens

    def __repr__(self):
        return f'TokenStorage "{self.token_name}": {self.tokens}'

    @property
    def token_num(self):
        if isinstance(self.tokens, list):
            return len(self.tokens)
        else:
            return self.tokens

    def get_token_pool(self) -> list:
        token_pool = []
        for token_type in self.tokens:
            token_pool += [token_type] * self.tokens[token_type]
        self.tokens = token_pool
        return self.tokens

    def limit_decorator(self):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if self.token_num+result not in self.limit:
                    return self.if_limit
                else:
                    return result
            return wrapper
        return decorator

    def try_change_token_num(self, num):
        @self.limit_decorator()
        def change(n) -> int | str:
            sum_ = self.token_num + n
            print(f'{self.tokens} + {n} -> {sum_}')
            return n
        return change(num)

    def change_tokens_by_(self, rolls: int = 0, draws: int = 0):
        for roll in range(rolls):
            add_tokens = choice(self.die)
            print(add_tokens)
            self.change_tokens_by_num(add_tokens)
        return self.tokens
    # попытка все запихнуть в рнд функцию

    def remove_token_from_list(self, token):
        if token in self.tokens:
            self.tokens.remove(token)
        else:
            print('No token!')
        return self

    def change_tokens_by_num(self,
                             token_num: int,
                             token_list: list = None):

        n = 1 if token_num > 0 else -1

        for i in range(abs(token_num)):
            result = self.try_change_token_num(n)
            if result == self.if_limit:
                print(f'Превышет лимит, происходит {self.if_limit}')
                return self.tokens
            else:
                if token_list:
                    if token_num > 0:
                        self.tokens.append(token_list[i])
                    else:
                        self.remove_token_from_list(token_list[i])
                else:
                    self.tokens += n

        return self.tokens

    def draw_from_pool(self, tokens: int) -> list:
        drawn = []
        for num in range(tokens):
            token = choice(self.tokens)
            drawn.append(token)
            result = self.c
            if result == self.if_limit:
                return result

        return drawn


ts = TokenStorage('EnergyPool',
                  {'ch': 5, 'ex': 5},
                  10,
                  limit=[0, 20],
                  if_limit='stop')
ts.get_token_pool()
print(ts)

for i in range(5):
    drawn_t = ts.draw_from_pool(tokens=3) # <- здесь нужен точно такой же счетчик
    print(drawn_t)
    ts.change_tokens_by_num(token_num=-1, token_list=['ex'])
    print(ts)
#
#vp = TokenStorage('VPs', 0)
#print(vp)
#vp.add_(tokens=2)
#print(vp)
#vp.spend_(2)
#print(vp)

#paradox = TokenStorage('ParadoxStorage',
#                       0,
#                       0,
#                       limit=[0, 3],
#                       if_limit='anomaly',
#                       die=[0, 1, 1, 1, 1, 2])
#print(paradox)
#a = paradox.add_tokens_by_die(rolls=3)
#print(a)
#if a == paradox.if_limit:
#    print('limit')
#    b = paradox.change_tokens_by_num(-paradox.tokens)
#    print(b)
#print(paradox)


#overage = paradox.add_(mod='by_die', rolls=3)
#paradox.spend_(1)
#print(paradox)
