import pandas as pd
from consts_and_funcs import path_to_project, load_frame_from_file
from random import shuffle
from chronology import Chronology


pd.set_option('display.max.columns', None)


class CronossusBoard:
    def __init__(self,
                 difficulty='easy',
                 game_build='original',
                 language='eng'):
        self.difficulty = difficulty
        self.game_build = game_build
        self.language = language

        self.board_frame = None
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

    def init_action_board(self):
        self.board_frame = load_frame_from_file(
            'action_board',
            path_to_project,
            index_col=0)

        action_tiles: pd.DataFrame = self.get_action_tiles()
        action_tiles.index = ['I', 'II', 'III']

        for place in action_tiles.index:
            self.board_frame = self.board_frame.replace(
                place,
                action_tiles.at[place, 'name'])

        return self.board_frame

    def init_chronology(self):
        df = load_frame_from_file(
            'chronology',
            path_to_project,
            index_col=0)

        self.chronology_deck = Chronology(
            chronology_frame=df,
            stage_name='era')

        self.chronology_deck.set_stage('1')

        return self.chronology_deck


chron = CronossusBoard(difficulty='medium')
chron.init_action_board()
chron.init_chronology()

