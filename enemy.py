from tupy import *


class Monstro (Image):
    """ 
    Classe que posciona a imagem do monstro no tabuleiro, é inicializada apenas no módulo "Home", quando o jogador se encontra na casa do inimigo. Determina o ataque do monstro selecionado, e sua respectiva força, sob um determinado jogador. Não retorna nada.
    """
    def __init__(self, monstro: str, forca: int, x:int, y:int) -> None:
        self._file = monstro + ".png"
        self.x = x 
        self.y = y
        self._forca = forca
        self._angle = 0

    @property
    def file(self):
        return self._file
    @property
    def angle(self):
        return self._angle
    @property
    def forca(self):
        return self._forca

#Era suposto ter o tipo do jogador escrito (self, jogador:Jogador), porém na hora da construção do código deu erro ao importar a classe "Jogador".
    def atacar(self, jogador) -> None:
        """
        Método que define as ações tomadas quando um jogador encontra um inimigo. Caso ele se encontre na casa do inimigo, e sua vida seja maior que a força do inimigo, o jogador vence e continua, se não for, volta para o início. Recebe como parâmentro o jogador que deve ser atacado,  não permite o monstro  atacar um jogador fora das casas determinadas. Não possui retorno.
        """
        if jogador._casa.numero in [3, 9, 16, 28, 33]:
            if jogador._vida > self._forca:
                toast("Parabéns! Você sobreviveu ao ataque!") 
                jogador._vida -= self._forca 
            else:
                jogador._casa.numero = 0
                jogador._x = 40 
                jogador._y = 115
                jogador._vida = 100 
                toast("Você perdeu!!") 
            jogador._vez = True 
            self._hide()
        else:
             toast("Você não pode atacar esse personagem!")
    