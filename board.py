from tupy import *

class Campo(Image):
    """
    Classe responsável por mapear cada casa do tabuleiro e seus respectivos valores do eixo x e y, atráves de um dicionário. Além de posicionar o arquivo da imagem do tabuleiro. Não retorna nada.
    """
    def __init__(self) -> None:
        self._file = 'fundo4.png' 
        self._x = 380 
        self._y = 230 
        self._angle = 0
        self._casas = {
            '1': {'x': 90, 'y': 115}, 
            '2': {'x': 162, 'y': 115}, 
            '3': {'x': 234, 'y': 115}, 
            '4': {'x': 306, 'y': 115}, 
            '5': {'x': 378, 'y': 115}, 
            '6': {'x': 450, 'y': 115}, 
            '7': {'x': 522, 'y': 115}, 
            '8': {'x': 594, 'y': 115}, 
            '9': {'x': 666, 'y': 115}, 
            '10': {'x': 738, 'y': 115},
            '11': {'x': 810, 'y': 115}, 
            '12': {'x': 810, 'y': 192}, 
            '13': {'x': 810, 'y': 269}, 
            '14': {'x': 738, 'y': 269}, 
            '15': {'x': 666, 'y': 269},
            '16': {'x': 594, 'y': 269},
            '17': {'x': 522, 'y': 269}, 
            '18': {'x': 450, 'y': 269}, 
            '19': {'x': 378, 'y': 269}, 
            '20': {'x': 306, 'y': 269}, 
            '21': {'x': 234, 'y': 269},
            '22': {'x': 162, 'y': 269}, 
            '23': {'x': 90, 'y': 269}, 
            '24': {'x': 90, 'y': 346},
            '25': {'x': 90, 'y': 423},
            '26': {'x': 162, 'y': 423},
            '27': {'x': 234, 'y': 423},
            '28': {'x': 306, 'y': 423},
            '29': {'x': 378, 'y': 423},
            '30': {'x': 450, 'y': 423},
            '31': {'x': 522, 'y': 423},
            '32': {'x': 594, 'y': 423},
            '33': {'x': 666, 'y': 423},
            '34': {'x': 740, 'y': 423},
        }
    @property
    def x(self):
         return self._x
    @property
    def y(self):
         return self._y
    @property
    def file(self):
         return self._file
    @property
    def angle(self):
         return self._angle
           