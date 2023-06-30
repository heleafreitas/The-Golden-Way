from tupy import *

class Monstro (Image):
    def __init__(self, monstro: str, forca: int, x:int, y:int):
        self.file = monstro + ".png" # Arquivo de imagem do monstro
        self.x = x # Coordenada x da imagem do monstro
        self.y = y # Coordenada y da imagem do monstro
        self.forca = forca
    
    def atacar(self, jogador) -> None:
        if jogador.vida > self.forca:
            toast("Parabéns! Você sobreviveu ao ataque!") # Exibe uma mensagem se o jogador sobreviveu ao ataque
            jogador.vida -= self.forca # Reduz a vida do jogador pela força do monstro
        else:
            jogador.casa.numero = 0
            # Move o jogador de volta para a posição inicial do tabuleiro
            jogador.x = 40
            jogador.y = 115
            jogador.vida = 100 # Define a vida do jogador de volta para 100 (vida inicial)
            toast("Você perdeu!!") # Exibe uma mensagem informando que o jogador perdeu
        jogador.vez = True # Define a vez do jogador como True para passar a vez para o próximo jogador
        self._hide() # Esconde a imagem do monstro após o ataque
    