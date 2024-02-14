from consts_and_funcs import load_frame_from_file


default_storages = 0


class PreparedAction:
    def __init__(self, action_like_string: str):

        string_list = action_like_string.split()
        self.answer = action_like_string
        self.action = string_list[0]
        self.storage = None
        self.subject = None

    def __repr__(self):
        return f'Prepare {self.answer}'

    @property
    def need_feedback(self):
        return self.action[-1] != 's'

    def get_answer_for_tg(self):
        ans = ['Chronossus']
        if self.need_feedback:
            ans.extend(['try to',
                          self.answer])
        else:
            ans.append(self.answer)
        return ' '.join(ans)

    def get_storage(self, storage_dict):
        pass


class PreparedConstruction(PreparedAction):
    def __init__(self, action_like_string):
        super().__init__(action_like_string)


action_frame = load_frame_from_file('action_deck', index_col=0)
print(action_frame)
for i in action_frame[1]:
    action = PreparedAction(i)
    print(action.action)
    answer = action.get_answer_for_tg()
    print(answer)


