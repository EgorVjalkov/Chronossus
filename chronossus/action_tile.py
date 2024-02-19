import pandas as pd
from consts_and_funcs import load_frame_from_file, path_to_project
from pathlib import Path


class ActionTile:
    def __init__(self, tile_data: pd.Series):
        self.name = tile_data['name']
        self.action = tile_data['action']
        self.autoleap = tile_data['autoleap']

    def __repr__(self):
        autoleap = f', autoleap' if self.autoleap else ''
        return f"{self.action}{autoleap}"
