class RowLenAnalyzer:
    def __init__(self, buttons: list):
        self.buttons = buttons
        self.rows = []
    # по 6 букв 4 кнопки

    def button_gen(self):
        for bnt in self.buttons:
            yield bnt

    @staticmethod
    def fit_in(symbols: int):
        if symbols > 20:
            return False
        return True

    def create_row_container(self) -> list:
        row = []
        bnt_gen = self.button_gen()
        for btn in bnt_gen:
            print(btn)
            symbols_count = len(''.join(row))
            if self.fit_in(symbols_count):
                row.append(btn)
            else:
                self.rows.append(row.copy())
                row.clear()
                row.append(btn)
        self.rows.append(row)
        return self.rows


