import pandas as pd
from random import shuffle
from chronology import Chronology, ActionsPath
from consts_and_funcs import (path_to_project,
                              load_frame_from_file,
                              prepare_action_frame,
                              save_frame_to_file)


pd.set_option('display.max.columns', None)


class Cronossus:
    def __init__(self,
                 difficulty='easy',
                 game_build='original',
                 language='eng'):
        self.difficulty = difficulty
        self.game_build = game_build
        self.language = language

        self.action_deck = None
        self.chronology_deck = Chronology

    def get_action_tiles(self) -> pd.DataFrame:
        tiles_frame = load_frame_from_file(
            'action_tiles',
            path_to_project)

        f_by_edition = tiles_frame[tiles_frame.game_build == self.game_build]

        if self.difficulty in ['easy', 'medium']:
            f_by_name = f_by_edition['name'].map(lambda i: '.A' in i)
            tiles = f_by_edition[f_by_name == True]

            if self.difficulty == 'medium':
                rnd_index = tiles.index.to_list()
                shuffle(rnd_index)
                tiles.index = rnd_index
        else:
            tiles = pd.DataFrame()
        return tiles

    def place_action_tiles(self):
        self.action_deck = load_frame_from_file(
            'action_deck',
            path_to_project,
            index_col=0)

        action_tiles: pd.DataFrame = self.get_action_tiles()
        action_tiles.index = ['I', 'II', 'III']

        for place in action_tiles.index:
            self.action_deck = self.action_deck.replace(
                place,
                action_tiles.at[place, 'name'])

        return self.action_deck

    def init_action_board(self):
        action_frames = []
        for marker in self.action_deck.index:
            action_frame = prepare_action_frame(chron.action_deck, marker)
            ap = ActionsPath(action_frame, f"({marker})")
            ap.set_stage(1)
            print(ap.construct_frame_for_concat())
            action_frames.append(ap.construct_frame_for_concat())
        self.action_deck = pd.concat(action_frames, axis=0)
        return self

    def init_chronology(self):
        chronology_frame = load_frame_from_file(
            'chronology',
            path_to_project,
            index_col=0)

        chronology = Chronology(chronology_frame)
        chronology.set_stage(1)
        self.chronology_deck = chronology.prapare_for_saving()

        return self.chronology_deck

    def save_chronossus_data(self):
        all_data = {'action_deck': self.action_deck,
                    'chronology': self.chronology_deck}
        for sheet_name in all_data:
            save_frame_to_file(all_data[sheet_name], sheet_name, path_to_project)



chron = Cronossus(difficulty='medium')
chron.place_action_tiles()
chron.init_action_board()
chron.init_chronology()
chron.save_chronossus_data()

#ap.set_stage(1)
#for i in range(6):
#    print(ap.stages)
#    print(ap.action)
#    ap.leap()
