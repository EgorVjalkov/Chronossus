building_menu_vars = ('expansions', 'difficulty', 'start session', 'abort')
expansions = ('FRACTURES OF TIME', 'DOOMSDAY', 'PIONEERS OF NEW EARTH', 'GUARDIANS OF THE COUNCIL', 'clear')
default_difficulty = ('easy', 'medium', 'hard')
manual_difficulty = []
game_build_dict = {'expansions': expansions, 'difficulty': default_difficulty}

non_build_combos = {
    'DOOMSDAY': ['FRACTURES OF TIME',
                 'PIONEERS OF NEW EARTH',
                 'GUARDIANS OF THE COUNCIL',
                 'HYPERSYNC FUTURE ACTIONS'],

    'FRACTURES OF TIME': ['GUARDIANS OF THE COUNCIL',
                          'DOOMSDAY'],

    'PIONEERS OF NEW EARTH': ['DOOMSDAY'],

    'GUARDIANS OF THE COUNCIL': ['DOOMSDAY',
                                 'FRACTURES OF TIME'],

    'HYPERSYNC FUTURE ACTIONS': ['DOOMSDAY']

}


class GameBuildCategory(object):

    def __init__(self, category_name_from_tg: str):
        self.name = category_name_from_tg

    @property
    def buttons(self):
        return game_build_dict[self.name]

    @property
    def article(self):
        if not self.name[-1] == 's':
            a_ = 'a'
        else:
            a_ = ''
        return a_

    @property
    def answer(self):
        return f'Choose {self.article} {self.name}.'
