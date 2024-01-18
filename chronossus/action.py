class Action:
    def __int__(self, name, autoleap=False):
        self.a_name = name
        self.autoleap = autoleap

    @property
    def need_feedback(self):
        return self.a_name[-1] != 's'
