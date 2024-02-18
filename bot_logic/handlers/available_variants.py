states_game_buildings = ['base game', 'expansions', 'difficulty']
base_games = ['ORIGINAL', 'FRACTURES OF TIME']
expansions = ['DOOMSDAY', 'PIONERS OF NEW EARTH', 'GUARDIANS OF THE COUNSIL', 'NO EXPANSIONS']
default_difficulty = ['easy', 'medium', 'hard']
manual_difficulty = []

game_build_dict = {'base game': base_games, 'expansions': expansions, 'difficulty': default_difficulty}


class GameBuildCategory(object):

    def __init__(self, category_name_from_tg: str):
        self.category_name = category_name_from_tg

    @property
    def buttons(self):
        return game_build_dict[self.category_name]

    @property
    def a(self):
        if not self.category_name[-1] == 's':
            a_ = 'a'
        else:
            a_ = ''
        return a_

    @property
    def answer(self):
        return f'Choose {self.a} {self.category_name}'
