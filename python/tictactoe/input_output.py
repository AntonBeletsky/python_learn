# ввод, вывод

# see at https://www.tutorialspoint.com/design_pattern/adapter_pattern.htm
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_adapter.htm

from console_io import ConsoleIO

class InputOutput(ConsoleIO):

    def __init__(self):
        pass

    # ввод имени

    # ввод координат
    def input_pos(self):
        xy = self.console_input_pos()
        return xy
        pass
pass
