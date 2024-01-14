import pandas as pd
from path_const import path_to_project
from pathlib import Path
from random import shuffle


pd.set_option('display.max.columns', None)


class CronossusBoard:
    def __init__(self,
                 difficulty='easy',
                 edition='essential',
                 language='eng'):
        self.difficulty = difficulty
        self.edition = edition
        self.language = language

        self.board_frame = None

    def get_action_tiles(self) -> dict:
        tiles_frame = self.load_frame_from_file('action_tiles')
        f_by_edition = tiles_frame[tiles_frame['edition'] == self.edition]
        if self.difficulty in ['easy', 'medium']:
            f_by_name = f_by_edition['name'].map(lambda i: '.A' in i)
            tiles = f_by_edition[f_by_name == True]
            if self.difficulty == 'medium':
                rnd_index = tiles.index.to_list()
                shuffle(rnd_index)
                tiles.index = rnd_index
        return tiles

    @staticmethod
    def load_frame_from_file(sheet_name, index_col=None) -> pd.DataFrame:
        path = Path(path_to_project, 'chronossus_action_board.xlsx')
        return pd.read_excel(path, sheet_name=sheet_name, index_col=index_col)

    def init_board(self):
        self.board_frame = self.load_frame_from_file(
            'action_board',
            index_col=0)

        action_tiles = self.get_action_tiles()
        action_tiles.index = ['I', 'II', 'III']

        for place in action_tiles.index:
            self.board_frame = self.board_frame.replace(
                place,
                action_tiles.at[place, 'name'])

        print(self.board_frame)


chr = CronossusBoard(difficulty='medium')
chr.init_board()
