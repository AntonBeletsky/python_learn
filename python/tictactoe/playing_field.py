# игровое поле
class PlayingField:

    # Матрица
    # 0 - пусто
    # 1 - крести
    # 2 - нолик
    matrix = [[0,0,0],[0,0,0],[0,0,0]]

    # инициализация
    def __init__(self=None):
        matrix = [[0,0,0],[0,0,0],[0,0,0]]
        pass

    # задать значение клетки
    def set_square(x, y, value, self=None):
        self.matrix[x,y] = value
        pass

    # получить значение клетки
    def get_square(x,y, self=None):
        return self.matrix[x,y]
        pass

    # походить
    def player_step(x, y, player=0, self=None):
        # клетка пуста
        if(self.get_square(x,y) == 0):
            # записать кто занял клетку
            self.set_square(x, y, v)
        else:
            return False
        pass

    # проверка выйграша player: [1,2] кого проверять крестик или нолик
    def check_winning(player=0, self=None):

        pass

    # общая проверка выйграша
    def check_winning(self):

        pass

    # движение по вектору, проверка значений в матрице по заданому параметру
    # start_x, end_x, start_y, end_y, стартовая позиция и конечная позиция
    # vector_x, vector_y, вектор напрвления
    # expected_value, ожидаемое значение
    # steps количество шагов
    # возвращает конкатацию результатов сравнения
    # @staticmethod
    def vector_motion(start_x, end_x,
                      start_y, end_y,
                      vector_x, vector_y,
                      expected_value, steps, self=None):

        counter = expected_value

        while start_x < end_x - start_x:
            while start_y < end_y - start_y:
                # берем значение из клетки
                temp_value = self.get_square(start_x, start_y)
                # сравниваем с параметром функции
                counter = (expected_value == temp_value)
                
                if (counter == False):
                    return False

                start_y += 1
                pass
            start_x += 1
        pass
