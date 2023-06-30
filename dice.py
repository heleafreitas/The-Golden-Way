from tupy import *
import random
from players import Jogador 

class Dado (Image):
  def __init__(self) -> None:
    self.file = 'dadoP.png' # Arquivo de imagem do dado
    self.x = 45 # Coordenada x da imagem do dado
    self.y = 35 # Coordenada y da imagem do dado
    self.faces = 6 # Número de faces do dado
    self.jogador = "" # Jogador que lançou o dado

  def jogarDado(self, jogador: Jogador) -> None:
    verificar = self.verificarVez(jogador)
    if verificar:
      jogador.vez = False
      n = random.randint(1,self.faces) # Gera um número aleatório entre 1 e o número de faces do dado
      toast(f"Você andou {n} casas") # Exibe a quantidade de casas que o jogador andou
      jogador.andar(n) # Move o jogador a quantidade de casas sorteada
      self.jogador = jogador # Armazena o jogador atual como o último a lançar o dado
    

  def verificarVez (self, jogador: Jogador) -> bool:
    if self.jogador == "":
      return True
    elif jogador != self.jogador:
      if jogador.casa.numero in [3, 9, 16, 28, 33] and jogador.vez == False:
        toast("Sobreviva ao ataque inimigo para continuar sua jornada!")
        return False
      else:
        if self.jogador.casa.numero in [3, 9, 16, 28, 33] and self.jogador.vez == False:
          return True
        else:
          self.jogador.vez = True
          return True
    else:
      toast("Não é a sua vez de jogar!")
      return False
