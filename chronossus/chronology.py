import pandas as pd


class Chronology:

    def __init__(self,
                 chronology_frame: pd.DataFrame,
                 token_value: str = '(*)'):

        self.frame_ = chronology_frame
        self.token_value = token_value
        self.default_stages = self.frame_.columns.to_list()

    def __repr__(self):
        for_print = self.stages.to_dict()
        for_print = [f'{i}{for_print[i]}' if for_print[i] else f'{i}'
                     for i in for_print]
        return ' | '.join(for_print)

    @property
    def limits(self):
        return self.default_stages[0], self.default_stages[-1]

    @property
    def stages(self):
        return pd.Series(data=self.frame_.columns,
                         index=self.default_stages,
                         dtype=str,
                         name=self.token_value).fillna('')

    @stages.setter
    def stages(self, new_stages: pd.Series) -> None:
        self.frame_.columns = new_stages

    @property
    def stage(self) -> int:
        stages = self.stages.index[self.stages == self.token_value].to_list()
        return stages[0]

    @property
    def stage_data(self):
        return self.frame_[self.token_value]

    def set_stage(self, stage: int | str) -> pd.Series:
        if stage == 'next':
            stage = self.stage + 1

        st_ser = pd.Series(index=self.stages.index, dtype=str).fillna('')
        st_ser.at[stage] = self.token_value
        self.stages = st_ser

        return self.stages

    def prapare_for_saving(self):
        stages = pd.DataFrame(self.stages.to_dict(),
                              index=[self.token_value])
        print(stages)
        data_frame = self.frame_
        data_frame.columns = self.default_stages
        print(data_frame)
        frame_ = pd.concat([stages, data_frame], axis=0)
        return frame_



class ActionsPath(Chronology):
    def __init__(self,
                 chronology_frame: pd.DataFrame,
                 token_value: str):
        super().__init__(chronology_frame, token_value)

    @property
    def marker(self) -> int:
        return self.frame_.index.to_list()[0]

    @property
    def action(self) -> str:
        return self.stage_data[self.marker]

    def leap(self) -> pd.Series:
        if self.stage == max(self.limits):
            return self.set_stage(1)
        else:
            return self.set_stage('next')

    def construct_frame_for_concat(self):
        data_ser = self.frame_.loc[self.marker]
        data_ser.index = self.default_stages
        frame_ = pd.concat([self.stages, data_ser], axis=1)
        return frame_.T
