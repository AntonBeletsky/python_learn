#base gamer class

class BaseGamer:

    # 1 - крестик, 2 - нолик
    player_identificator = 0

    #инициализация
    def __init__(self, player_identificator):
        self.player_identificator = player_identificator
        pass

    # Ход игрока (переопределеяеться в наследнике)
    def  player_step(self):
        # получеие координат
        x = -1
        y = -1
        return [x, y, self.player_identificator]
        pass
pass



