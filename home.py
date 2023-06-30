import random
from enemy import *


class Casa:
    def __init__(self, campo) -> None:
        self.numero = 0 # Número da casa
        self.campo = campo # Referência ao objeto Campo

    def verificar_casa(self) -> list[int]:
        resultado = [3, 0] # Resultado padrão para uma casa comum
        if self.numero in [7, 14, 23, 30]:
            resultado = self.casa_surpresa() # Casa surpresa "?"
        elif self.numero in [5, 19, 26]:
            resultado = self.casa_da_sorte() # Casa da sorte "S2"
        elif self.numero in [3, 9, 16, 28, 33]:
            resultado = [2,0] # Casa do inimigo "!"
            self.casa_do_inimigo()
        return resultado
        
    
    def casa_surpresa(self) -> list[int]:
        decisao = random.randint(0,1) # Sorteia um número 0 ou 1 para representar uma decisão na casa surpresa
        if decisao == 0:
            recompensa = random.choice([-3,-2, -1, 1, 2, 3]) # Sorteia uma recompensa negativa ou positiva
            if recompensa > 0:
                toast(f"Parabéns, você chegou na casa surpresa e avançou {recompensa} casas")
            else:
                toast(f"Que pena, você chegou na casa surpresa e voltou {abs(recompensa)} casas")
        else:
            recompensa = random.choice([-50,50]) # Sorteia uma recompensa negativa ou positiva
            if recompensa > 0:
                toast(f"Parabéns, você chegou na casa surpresa e ganhou {recompensa} de vida")
            else:
                toast(f"Que pena, você chegou na casa surpresa e perdeu {abs(recompensa)} de vida")
        resultado = [decisao, recompensa]
        return resultado

    def casa_da_sorte(self) -> list[int]:
        toast(f"Parabéns, você chegou na casa da sorte e ganhou 50 de vida")
        resultado = [1, 50]
        return resultado # Resultado para a casa da sorte
    
    def casa_do_inimigo(self) -> Monstro:
        tipo = random.choice(["ogro", "troll"]) # Sorteia um tipo de monstro a ser enfrentado (ogro ou troll)
        if tipo == "ogro":
            forca = 80 # Força do monstro ogro
        else:
            forca = 50 # Força do monstro troll
        x =  self.campo.casas[str(self.numero)]['x'] # Obtém a coordenada x da posição da casa no tabuleiro
        y = self.campo.casas[str(self.numero)]['y'] # Obtém a coordenada y da posição da casa no tabuleiro
        inimigo = Monstro(tipo, forca, x, y) # Cria um objeto Monstro com base no tipo, força e posição
        toast("Oh não! Você encontrou um monstro no caminho, faça de tudo para continuar sua aventura!")
        