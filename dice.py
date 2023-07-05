from tupy import *
import random
from players import Jogador 

class Dado (Image):
  """ 
  Classe que posciona a imagem do dado no tabuleiro, e determina qual jogador está apto para jogar o dado e qual vai andar um certo número de casas. Não retorna nada.
  """
  def __init__(self) -> None:
    self._file = 'dadoP.png' 
    self._x = 45 
    self._y = 35 
    self._faces = 6 
    self._jogador = "" 
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
  def y(self):
    return self._y
    

  def jogarDado(self, jogador: Jogador) -> None:
    """ 
    Método que verifica se é a vez do jogador por meio da chamada da outra função "VerificarVez", caso essa retorne Verdadeiro, faz com que o jogador recebido como parâmentro ande um valor aleátorio de 1 a 6 casas. Passa o valor obtido para o método 'andar' da classe ""Jogador". Não retorna nada.
    """
    verificar = self._verificarVez(jogador)
    if verificar:
      jogador._vez = False
      n = random.randint(1,self._faces) 
      toast(f"Você andou {n} casas") 
      jogador._andar(n) 
      self._jogador = jogador 

      
    

  def _verificarVez (self, jogador: Jogador) -> bool:
    """
    Método responsável por chegar se é a vez de um jogador, não permitindo que ele jogue o dado duas vezes seguidas, nem jogue o dado antes de vencer o inimigo. Retorna um valor booleano que determina se é ou não a vez do jogador.
    """
    if self._jogador == "":
      return True
    elif jogador != self._jogador:
      if jogador._casa.numero in [3, 9, 16, 28, 33] and jogador._vez == False:
        toast("Sobreviva ao ataque inimigo para continuar sua jornada!")
        return False
      else:
        if self._jogador._casa.numero in [3, 9, 16, 28, 33] and self._jogador._vez == False:
          return True
        else:
          self._jogador._vez = True
          return True
    else:
      toast("Não é a sua vez de jogar!")
      return False
