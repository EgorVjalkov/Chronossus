import pandas as pd
from chronossus.classes.tokenstorage import TokenStorage


class Chronology(TokenStorage):

    def __init__(self,
                 chronology_name: str,
                 stages: list,
                 stage: int = 1):

        super().__init__(chronology_name, stage)

        self.valid_values = stages

    def __repr__(self):
        for_print = self.marker_ser.to_dict()
        for_print = [f'{for_print[i]}' if for_print[i] else f'{i}'
                     for i in for_print]
        return ' | '.join(for_print)

    @property
    def marker_ser(self) -> pd.Series:
        ser = pd.Series(index=self.valid_values, dtype=str, name=self.name)
        ser[self.value] = self.marker
        return ser.fillna('')

    def go_for_(self, stages=1) -> int:
        return self.change_value_by_(num=stages)

    def stage_data(self, pd_data: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
        return pd_data[self.value]

    def prapare_for_saving(self, data_frame) -> pd.DataFrame:
        stages = pd.DataFrame(self.marker_ser.to_dict(),
                              index=[self.marker])
        data_frame.columns = self.valid_values
        frame_ = pd.concat([stages, data_frame], axis=0)
        return frame_


chronology_line = Chronology('chronology',
                             [1, 2, 3, 4, 5, 6])


class Track(Chronology):
    def __init__(self,
                 track_name: str,
                 stage_data: pd.Series,
                 stage: int = 1):

        super().__init__(chronology_name=track_name,
                         stages=stage_data.index.to_list(),
                         stage=stage)

        self.stages_data = stage_data

    @property
    def data(self) -> str:
        return self.stage_data(self.stages_data)

    def prapare_for_saving(self, **kwargs):
        frame_ = pd.concat([self.marker_ser, self.stages_data], axis=1)
        return frame_.T


class CommandTrack(Track):
    def __init__(self,
                 track_name: str,
                 stage_data: pd.Series,
                 stage: int = 1):

        super().__init__(track_name,
                         stage_data,
                         stage)

        self.recursion = True
