import pandas as pd
from tokenstorage import TokenStorage


class Chronology(TokenStorage):

    def __init__(self,
                 chronology_name: str,
                 stages: list,
                 if_limit: str = 'stop'):

        default_value = stages[0]

        super().__init__(chronology_name,
                         default_value,
                         if_limit=if_limit)

        self.valid_values = stages

    @property
    def stages_ser(self):
        ser = pd.Series(index=self.valid_values, dtype=str, name=self.name)
        ser[self.value] = self.marker
        return ser.fillna('')

    def stage_data(self, data_frame):
        return data_frame[self.value]

    def prapare_for_saving(self, data_frame):
        stages = pd.DataFrame(self.stages_ser.to_dict(),
                              index=[self.marker])
        print(stages)
        data_frame.columns = self.valid_values
        print(data_frame)
        frame_ = pd.concat([stages, data_frame], axis=0)
        return frame_


chronology_line = Chronology('chronology',
                             [1, 2, 3, 4, 5, 6, 7])

#  нужно подумать как возбуждать лимитирование. через декоратор чтольб?

#    def __repr__(self):
#        for_print = self.stages.to_dict()
#        for_print = [f'{i}{for_print[i]}' if for_print[i] else f'{i}'
#                     for i in for_print]
#        return ' | '.join(for_print)

#


#class ActionsPath(Chronology):
#    def __init__(self,
#                 chronology_frame: pd.DataFrame,
#                 token_value: str):
#        super().__init__(chronology_frame, token_value)
#
#    @property
#    def marker(self) -> int:
#        return self.frame_.index.to_list()[0]
#
#    @property
#    def action(self) -> str:
#        return self.stage_data[self.marker]
#
#    def leap(self) -> pd.Series:
#        if self.stage == max(self.limits):
#            return self.set_stage(1)
#        else:
#            return self.set_stage('next')
#
#    def construct_frame_for_concat(self):
#        data_ser = self.frame_.loc[self.marker]
#        data_ser.index = self.default_stages
#        frame_ = pd.concat([self.stages, data_ser], axis=1)
#        return frame_.T
