import pandas as pd
from consts_and_funcs import load_frame_from_file, path_to_project
from pathlib import Path


class ActionTile:
    def __init__(self, name: str):
        self.name = name
        self.data: pd.Series = load_frame_from_file(
            'action_tiles',
            path=path_to_project, # <-- хз почему но путь гуляет как ему хочется
            index_col=0
        ).loc[self.name]


tile = ActionTile('C01.A')
print(tile.data)
