from chronossus.complex_storage import ComplexStorage


#paradox = TokenStorage('paradox',
#                       0,
#                       [0, 3],
#                       'anomaly',
#                       die=[0, 1, 1, 1, 1, 2])
#
#paradox.change_token_num_by_(die=True, rolls=15)
#
#
#paradox.change_token_num_by_(num=2)
#print(paradox)
#paradox.change_token_num_by_(num=-2)
#print(paradox)


b = ComplexStorage('Breakthroughs',
                   {'[]': 0, '/\\': 0, '( )': 0},
                   [0, 20],
                   if_limit='stop',
                   die=['[ ]', '/\\', '( )'])

print(b)
print(b.token_pool)
b.change_token_pool_by_(action='add', die_rolls=1)
print(b)
b.change_token_pool_by_(token_list=[b.last_token], action='rm')
print(b)



#
#for i in range(10):
#    drawn_t = ts.draw_tokens_from_pool(draws=3) # <- здесь нужен точно такой же счетчик
#    print(drawn_t)
#    ts.change_tokens_manually(token_num=+1, token_list=['ex'])
#    print(ts)
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
