class Action:
    def __int__(self, name, autoleap=False):
        self.a_name = name
        self.autoleap = autoleap

    @property
    def action_character(self):
        if self.a_name[-1] == 's':
            return 'simple'
        else:
            return 'feedback'

    def
