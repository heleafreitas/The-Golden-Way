from tupy import *
from board import Campo
from home import Casa


class Jogador (Image):
    """
    Classe responsável por posicionar os jogadores no tabuleiro. Recebe como parêmentro o nome do personagem (fada ou duende), a função 'Campo' e 'Casa' que possibilitam a movimentação dos jogadores pelo tabuleiro e identificação das casas especiais. Possui como atributo a vida de cada jogador e a sua vez (se está habilitado a andar). Não retorna nenhum valor.
    """
    def __init__(self, personagem: str, campo: Campo, casa: Casa) -> None:
        self._file = personagem + ".png" 
        self._x = 40 
        self._y = 115 
        self._vida = 100
        self._casa = casa
        self._campo = campo
        self._vez = True 
        self._angle = 0

    @property
    def file(self):
        return self._file
    @property
    def angle(self):
        return self._angle
    @property
    def x(self):
        return self._x
           
    @property
    def vida(self):
        return self._vida
    
    @property
    def y(self):
        return self._y
        
    def _andar (self, qtd: int) -> None:
        """
        Método que permite a movimentação do jogador pelo tabuleiro. Recebe como parâmetro a quantidade de casas que devem ser pecorridas de acordo com o valor obtido no método 'jogarDado'. Caso o jogador chegue ao final do tabuleiro, exibe a mensagem que indica que o jogador venceu jogo. Além disso, executa os resultados e suas devidas recompensas obtidas na classe 'Casa'. Retorna None.
        """
        self._casa.numero += qtd
        if self._casa.numero >= 34:
            self._x = 740
            self._y = 423
            toast("Você achou o baú de ouro no final do arco-íris!") 
        else:
            self._x = self._campo._casas[str(self._casa.numero)]['x'] 
            self._y = self._campo._casas[str(self._casa.numero)]['y'] 

        resultado = self._casa.verificar_casa() 

        
        if resultado[0] == 0:
            self._andar(resultado[1])
        elif resultado [0] == 1:
            self._vida += resultado[1] 
        elif resultado[0] == 2:
            self._vez = False  