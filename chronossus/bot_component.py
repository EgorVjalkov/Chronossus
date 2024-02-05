from abc import ABCMeta, abstractmethod
import pandas as pd


class BaseComponent(metaclass=ABCMeta):
    def __init__(self,
                 name: str,
                 default_value: int,
                 limit: int,
                 if_limit: str):
        self.name = name
        self.default_value = default_value
        self.limit = limit
        self.if_limit = if_limit

        self.marker = self.default_value

    @property
    def stages(self):
        stages = list(range(self.default_value, self.limit))
        stages_d = {stages[i]: None for i in stages}
        return pd.Series(dtype=str, index=stages, name=self.name).fillna('')
    # делаю суперкласс, который базовый и вмещает в себя особенности и хранильщ токенов и лент хронологии

    @stages.setter
    def stages(self, new_stages: pd.Series) -> None:
        self.frame_.columns = new_stages

    def set_stage(self, stage: int | str) -> pd.Series:
        if stage == 'next':
            stage = self.stage + 1

        st_ser = pd.Series(index=self.stages.index, dtype=str).fillna('')
        st_ser.at[stage] = self.token_value
        self.stages = st_ser

        return self.stages


