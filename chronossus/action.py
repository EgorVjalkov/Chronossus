from tokenstorage import TokenStorage
from complex_storage import ComplexStorage


# акции бывают разные. с выбором, напирмер
class Action:

    def __init__(self,
                 name: str,
                 storage: TokenStorage | ComplexStorage,
                 autoleap: bool = False):

        self.a_name = name
        self.storage = storage

        self.autoleap = autoleap
        self.done = False

    def is_done(self, player_answer):
        if player_answer == 'done':
            self.done = True
        return self.done

    def acomplish(self):
        pass

    @staticmethod
    def spend_EXO(exos_storage: TokenStorage):
        exos_storage.change_value_by_(num=-1)
        return exos_storage


core_pool = ComplexStorage('powercore',
                           {'ch': 5, 'ex': 5},
                           [0, 20])

act = 'gains a powercore'

list = ['ch']

act = Action(name=act.split()[0],
             storage=core_pool)
print(act.need_feedback)


