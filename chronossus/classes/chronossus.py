import pandas as pd
from random import shuffle
from consts_and_funcs import (path_to_project,
                              load_frame_from_file,
                              prepare_action_frame,
                              save_frame_to_file)
<<<<<<< HEAD:chronossus/chronossus.py
from chronossus.chronology import Chronology, CommandTrack
from chronossus.action_tile import ActionTile

=======
from chronossus.classes.chronology import Chronology, CommandTrack
>>>>>>> refs/remotes/origin/main:chronossus/classes/chronossus.py

pd.set_option('display.max.columns', None)


class Chronossus:
    def __init__(self,
                 base_game: str = 'ORIGINAL',
                 expansions: str = 'NO EXPANSIONS',
                 difficulty: str = 'easy',
                 language: str = 'eng'):

        self.base_game = base_game
        self.expansions = expansions
        self.difficulty = difficulty
        self.language = language

        self.action_board = None
        self.chronology_deck = None
        self.objectives = None

    def __repr__(self):
        return f"Chronossus build: {self.base_game}, {self.expansions}, {self.difficulty}"

    def load_sheet_and_filter_by_game_build(self,
                                            sheet_name: str) -> pd.DataFrame:
        sheet = load_frame_from_file(
            sheet_name,
            path_to_project)

        f_by_edition = sheet[sheet.game_build == self.base_game]
        return f_by_edition

    def init_objectives(self):
        obj_frame = self.load_sheet_and_filter_by_game_build('objectives')
        rnd_index = obj_frame.index.to_list()
        shuffle(rnd_index)
        obj_frame.index = rnd_index
        self.objectives = obj_frame.sort_index().head(3).set_index('name')
        del self.objectives['game_build']
        return self.objectives

    def get_action_tiles(self) -> pd.DataFrame:
        tiles_frame = self.load_sheet_and_filter_by_game_build('action_tiles')

        if self.difficulty in ['easy', 'medium']:
            f_by_name = tiles_frame['name'].map(lambda i: '.A' in i)
            tiles = tiles_frame[f_by_name == True]

            if self.difficulty == 'medium':
                rnd_index = tiles.index.to_list()
                shuffle(rnd_index)
                tiles.index = rnd_index
        else:
            tiles = pd.DataFrame()
        return tiles

    def place_action_tiles(self):
        self.action_board = load_frame_from_file(
            'action_deck',
            path_to_project,
            index_col=0)

        action_tiles: pd.DataFrame = self.get_action_tiles()
        action_tiles.index = ['I', 'II', 'III']

        for place in action_tiles.index:
            tile = ActionTile(action_tiles.loc[place])
            self.action_board = self.action_board.replace(
                place,
                tile)

        return self.action_board

    def init_action_board(self):
        action_frames = []
        for marker in self.action_board.index:
            action_frame = prepare_action_frame(self.action_board, marker)
            ap = CommandTrack(str(marker), action_frame.loc[marker])
            action_frames.append(ap.prapare_for_saving())
        self.action_board = pd.concat(action_frames, axis=0)
        return self

    def init_chronology(self):
        chronology_frame = load_frame_from_file(
            'chronology',
            path_to_project,
            index_col=0)

        chronology = Chronology(chronology_name='chronology',
                                stages=chronology_frame.columns.to_list())
        self.chronology_deck = chronology.prapare_for_saving(chronology_frame)

        return self.chronology_deck

    def save_chronossus_data(self):
        all_data = {'objectives': self.objectives,
                    'action_deck': self.action_board,
                    'chronology': self.chronology_deck}
        for sheet_name in all_data:
            save_frame_to_file(all_data[sheet_name], sheet_name)


