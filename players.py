from tupy import *
from board import Campo
from home import Casa

#Jogador Fada anda na X = 72 na primeira linha, em que Y = 115
#Jogador Fada final primeira linha Y = 115 X = 810
#Início X = 40 e Y = 115
#Jogador Fada para baixo Y = 77
#Jogador Fada X = 90 e Y = 269 segunda curva, final segunda linha 
#Jogador Fada X = 666 e Y = 432 ultima linha 
#Fim do tabuleiro X= 740

class Jogador (Image):
    def __init__(self, personagem: str, campo: Campo, casa: Casa) -> None:
        self.file = personagem + ".png" # Arquivo de imagem do jogador
        self.x = 40 # Coordenada x da imagem do jogador
        self.y = 115 # Coordenada y da imagem do jogador
        self.vida = 100 # Vida do jogador
        self.casa = casa
        self.campo = campo
        self.vez = True # Indica se é a vez do jogador

    def andar (self, qtd: int) -> None:
        self.casa.numero += qtd # Atualiza o número da casa com base na quantidade de casas a andar do tabuleiro
        if self.casa.numero >= 34:
            self.x = 740
            self.y = 423
            toast("Você achou o baú de ouro no final do arco-íris!") # Exibe uma mensagem se o jogador chegou ao final do tabuleiro
        else:
            self.x = self.campo.casas[str(self.casa.numero)]['x'] # Atualiza a coordenada x do jogador com base na posição da casa
            self.y = self.campo.casas[str(self.casa.numero)]['y'] # Atualiza a coordenada y do jogador com base na posição da casa

        resultado = self.casa.verificar_casa() # Verifica a casa em que o jogador parou
 
        if resultado[0] == 0:
            self.andar(resultado[1]) # Se o resultado for 0, significa que o jogador deve andar novamente
        elif resultado [0] == 1:
            self.vida += resultado[1] # Se o resultado for 1, o jogador ganha vida
        elif resultado[0] == 2:
            self.vez = False # Se o resultado for 2, é a vez do próximo jogador