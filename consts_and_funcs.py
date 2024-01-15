from pathlib import Path
import pandas as pd


path_to_project = Path.cwd()


def load_frame_from_file(sheet_name, path, index_col=None) -> pd.DataFrame:
    path = Path(path, 'chronossus_action_board.xlsx')
    return pd.read_excel(path, sheet_name=sheet_name, index_col=index_col)
