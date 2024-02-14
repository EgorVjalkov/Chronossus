import os
from pathlib import Path
import pandas as pd


path_to_project = Path(os.path.dirname(os.path.abspath(__file__)))


def load_frame_from_file(sheet_name: str,
                         path: Path = None,
                         index_col=None) -> pd.DataFrame:
    path = Path(path_to_project, 'chronossus', 'chronossus_action_board.xlsx')
    return pd.read_excel(path, sheet_name=sheet_name, index_col=index_col)


def save_frame_to_file(frame: pd.DataFrame,
                       sheet_name: str,
                       path: Path = None) -> None:
    path_to_dir = Path(path_to_project, 'output')
    file_name = 'chronossus_after_init.xlsx'
    path_to_file = Path(path_to_dir, file_name)
    if file_name in os.listdir(path_to_dir):
        mode = 'a'
        if_sheet_exist = 'replace'
    else:
        mode = 'w'
        if_sheet_exist = None

    with pd.ExcelWriter(
            path_to_file,
            mode=mode,
            if_sheet_exists=if_sheet_exist
    ) as writer:
        frame.to_excel(writer, sheet_name)


def prepare_action_frame(frame_: pd.DataFrame,
                         index: int | str,
                         nan_filter: bool = False):
    frame_ = frame_[frame_.index == index]
    if nan_filter:
        mapped = frame_.map(pd.isna)
        frame_ = frame_[mapped.index[mapped == False]]
    return frame_

