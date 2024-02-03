import pandas as pd


class Chronology:

    def __init__(self,
                 chronology_frame: pd.DataFrame,
                 stage_name: str):

        self.frame = chronology_frame
        self.stage_name = stage_name
        self.default_stages = self.frame.columns

    def __repr__(self):
        for_print = self.stages.to_dict()
        for_print = [f'{i}{for_print[i]}' if for_print[i] else f'{i}'
                     for i in for_print]
        return ' | '.join(for_print)

    @property
    def stages(self):
        return pd.Series(data=self.frame.columns,
                         index=self.default_stages,
                         dtype=str,
                         name='stages').fillna('')

    @stages.setter
    def stages(self, new_stages: pd.Series) -> None:
        self.frame.columns = new_stages

    @property
    def stage(self) -> int:
        stages = self.stages.index[self.stages == '*'].to_list()
        return stages[0]

    @property
    def stage_storage(self):
        return self.frame['*']

    def set_stage(self, stage: int | str) -> pd.Series:
        if stage == 'next':
            stage = self.stage + 1

        st_ser = pd.Series(index=self.stages.index, dtype=str).fillna('')
        st_ser.at[stage] = '*'
        self.stages = st_ser

        return self.stages

    def get_stage_storage(self, stage: int = None):
        if stage:
            self.set_stage(stage)
        return self.stage_storage
