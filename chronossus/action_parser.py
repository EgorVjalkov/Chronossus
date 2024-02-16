import pandas as pd

from consts_and_funcs import load_frame_from_file


class PreparedAction:
    def __init__(self,
                 action_like_string: str,
                 era: int):

        self.action = action_like_string
        self.era = era
        self.storage_frame = None
        self.era_values = None

    def __repr__(self):
        return f'Prepare {self.action}'

    @property
    def need_exosuit(self):
        return self.action[-1] != 's'

    def get_answer_for_tg(self):
        ans = ['Chronossus']
        if self.need_exosuit:
            ans.extend(['try to',
                        self.action])
        else:
            ans.append(self.action)
        return ' '.join(ans)

    def get_storages(self) -> pd.DataFrame:
        default_storages = load_frame_from_file('default_token_storage', index_col=0)
        print(default_storages)
        storages_by_action = default_storages['action'].map(lambda i: self.action in [i])
        self.storage_frame = default_storages[storages_by_action == True]
        if self.need_exosuit:
            self.storage_frame = pd.concat([default_storages['Exosuits':'Exosuits'],
                                            self.storage_frame])
        return self.storage_frame

    def get_era_values(self, era_storage: pd.Series):
        era_storage = load_frame_from_file('chronology', index_col=0)
        # остановился на загрузке из ленты хронологии


class PreparedConstruction(PreparedAction):
    def __init__(self, action_like_string):
        super().__init__(action_like_string)


action_frame = load_frame_from_file('action_deck', index_col=0)
print(action_frame)
for i in action_frame[1]:
    action = PreparedAction(i, 2)
    print(action.action)
    answer = action.get_answer_for_tg()
    print(answer)
    action.get_storages()
    break


