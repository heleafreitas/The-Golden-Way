from tupy import *
from board import Campo
from home import Casa
from dice import *
from players import *
from enemy import *
        
if __name__ == '__main__':
  campo = Campo() 
  casa = Casa(campo) 
  casa2 = Casa(campo) 
  fada = Jogador("fada", campo, casa) 
  duende = Jogador("duende", campo, casa2) 
  dado = Dado() 

run(globals()) 

