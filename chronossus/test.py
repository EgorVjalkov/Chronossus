from chronossus.classes.chronology import CycledTrack
import pandas as pd


#paradox = TokenStorage('paradox',
#                       0,
#                       3,
#                       die=[0, 1, 1, 1, 1, 2])
#
#paradox.change_value_by_(die=True, rolls=2)
#print(paradox)
#
#
#paradox.change_value_by_(num=-3)
#print(paradox)

#b = ComplexStorage('Breakthroughs',
#                   [],
#                   20,
#                   die=['[ ]', '/\\', '( )'])
#
#print(b)
#b.change_token_pool_by_(action='add', die_rolls=1)
#print(b)
#b.change_token_pool_by_(token_list=[b.last_token]*2, action='rm')
#print(b)
#b.change_token_pool_by_(draws=3)
#print(b)
#print(b.drawn)


#ch = Chronology('Chronology_line',
#                [1, 2, 3, 4, 5, 6, 7])
#print(ch)
#ch.go_for_(2)
#print(ch)
#
#a = TimeTravelTrack('timetravel',
#                    pd.Series({1: 0, 2: 2}, name='VP'))
#
#print(a)
#a.go_for_(1)
#print(a.data)
#print(a.prapare_for_saving())
#

a = CycledTrack('1',
                pd.Series({1: 'x', 2: 'y'}, name='action'),
                stage=2)

print(a)
a.go_for_(-2)
print(a.data)
print(a.prapare_for_saving())
