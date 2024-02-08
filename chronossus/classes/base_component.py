import pandas as pd



class BaseComponent(object):

    @staticmethod
    def get_valid_values(limit) -> list:
        return list(range(*limit))

    def __init__(self,
                 name: str,
                 default_value: int,
                 limit: list,
                 if_limit: str):
        self.name = name
        self.default_value = default_value
        self.valid_values = self.get_valid_values(limit)
        self.if_limit = if_limit

        self.marker = f'({self.name[0].upper()})'
        self.value = default_value

    def __repr__(self):
        return f'{self.marker}: {self.value}'

    def is_valid(self, new_value):
        return new_value in self.valid_values

    def get_value_if_valid(self, num) -> int:
        if self.is_valid(num):
            return num
        else:
            self.if_limit_func()
            return self.value

    def if_limit_func(self):
        print(self.if_limit)
        raise StopIteration()

    def stop_iteration_decor(self):
        def decor(func):
            def wrapper(*args, **kwargs):
                try:
                    value = func(*args, **kwargs)
                except StopIteration:
                    return self.value

                self.value = value
                return self.value

            return wrapper

        return decor

    @property
    def stages(self):
        stages = list(range(self.default_value, self.limit))
        stages_d = {stages[i]: '' for i in stages}
        return pd.Series(stages_d, dtype=str, index=stages, name=self.name)
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


