import pandas as pd


class Chronology:
    def __init__(self,
                 chronology_frame: pd.DataFrame,
                 stage_name: str):
        self.frame = chronology_frame
        self.stage_name = stage_name
        self.default_stages = [str(i) for i in
                               self.frame.columns.to_list()]

    def __repr__(self):
        return f"{self.stages.to_list()}"

    @property
    def stages(self):
        return pd.Series(self.frame.columns, dtype=str, name='stages')

    @stages.setter
    def stages(self, eras_list):
        self.frame.columns = pd.Series(eras_list, dtype=str, name='stages')

    @property
    def stage(self) -> str:
        stages = [i for i in self.stages if '*' in str(i)]
        return stages[0]

    @property
    def stage_num(self) -> int:
        return int(self.stage.replace('*', ''))

    @property
    def stage_storage(self):
        return self.frame[self.stage]

    def set_stage(self, stage: str) -> pd.Series:
        if stage == 'next':
            stage = str(self.stage_num + 1)

        self.stages = [f"*{i}" if i == stage else i
                       for i in self.default_stages]
        return self.stages

    def get_stage_storage(self, stage: str = None):
        if stage:
            self.set_stage(stage)
        return self.stage_storage
