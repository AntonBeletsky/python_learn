class ConsoleIO:

    def __init__(self):
        self.str_x = '''|* *|
| * |
|* *|'''
        self.str_o = '''| * |
|* *|
| * |'''
        self.str_null = '''   
   
   '''
        self.line = "\n*---**---**---*"
        self.border = "|"

        self.text_matrix = ""
        pass

    # ввод имени

    #ввод числа
    def input_val(self, str):
        print(str)
        return input()
        pass

    # ввод координат
    def console_input_pos(self):

        t_x = self.input_val("Введите X от 1 до 3")
        t_y = self.input_val("Введите Y от 1 до 3")

        x = t_x 
        y = t_y

        return [x, y]
        pass

    # отрисовка крестиков и ноликов
    def render_matrix_2(self, matrix = [[0,0,0],[0,0,0],[0,0,0]]):
        for x in range(3):
            print(self.line)
            for y in range(3):
                print("x,y, m:", x, y, matrix[x][y])
                if(matrix[x][y] == 0):
                    print(self.str_null)
                elif(matrix[x][y] == 1):
                    print(self.str_x)
                elif(matrix[x][y] == 2):
                    print(self.str_o)
                else:
                    print("не сработало условие")
                pass
        pass

    def writeXO(self, player=0, x=0, y=0):
        # self.text_matrix 


        pass

    # отрисовка крестиков и ноликов
    def render_matrix(self, matrix = [[0,0,0],[0,0,0],[0,0,0]]):
        result_text = "" # обрабатывать как двумерный массив
        x = 0
        while x < 3:
            print(self.line)
            y = 0
            # заменить на формирование строки 3*(9+2)
            while y < 3:
                print("x,y:", x, y)
                if(matrix[x][y] == 0):
                    print(self.str_null, end='')
                elif(matrix[x][y] == 1):
                    print(self.str_x, end='')
                elif(matrix[x][y] == 2):
                    print(self.str_o, end='')
                else:
                    print("не сработало условие")
                y += 1
                pass
            x += 1
            
        pass

pass
