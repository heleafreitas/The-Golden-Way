from tupy import *
from board import Campo
from home import Casa
from dice import *
from players import *
from enemy import *
        
if __name__ == '__main__':
  campo = Campo() # Cria o objeto Campo
  casa = Casa(campo) # Cria o objeto Casa para o primeiro jogador
  casa2 = Casa(campo) # Cria o objeto Casa para o segundo jogador
  fada = Jogador("fada", campo, casa) # Cria o primeiro jogador com o personagem "fada"
  duende = Jogador("duende", campo, casa2) # Cria o segundo jogador com o personagem "doende"
  dado = Dado() # Cria o objeto Dado

run(globals()) # Executa o jogo