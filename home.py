import random
from enemy import *
from board import *


class Casa:
    """
    Classe responsável por mapear as casas especiais; surpresa, sorte e do inimigo. Recebe a classe 'Campo' como parâmentro. Não retorna nada.
    """
    def __init__(self, campo: Campo) -> None:
        self.numero = 0 
        self.campo = campo 

    def verificar_casa(self) -> list[int]:
        """ 
        Método que verifica se o jogador se encontra nas casas especiais de acordo com os valores das chaves do dicionário do módulo 'Board'. Retorna uma lista de inteiros, cujo valores variam de acordo com a casa especial.
        """
        resultado = [3, 0] 
        if self.numero in [7, 14, 23, 30]:
            resultado = self.casa_surpresa() 
        elif self.numero in [5, 19, 26]:
            resultado = self.casa_da_sorte() 
        elif self.numero in [3, 9, 16, 28, 33]:
            resultado = [2,0] 
            self.casa_do_inimigo()
        return resultado
        
    
    def casa_surpresa(self) -> list[int]:
        """ 
        Método que determina o comportamento da casa supresa. De forma aleatória, o jogador pode andar ou voltar um certo número de casas (também aleatório) ou pode ganhar ou peder 50 de vida. Retorna uma lista de inteiros, que primeiro possui um valor que representa qual dos casos foi escolhido (1, ganho/perda de vida, ou 0, andar/voltar casas) e qual o valor da recompensa (casas ou vida).
        """
        decisao = random.randint(0,1) 
        if decisao == 0:
            recompensa = random.choice([-3,-2, -1, 1, 2, 3]) 
            if recompensa > 0:
                toast(f"Parabéns, você chegou na casa surpresa e avançou {recompensa} casas")
            else:
                toast(f"Que pena, você chegou na casa surpresa e voltou {abs(recompensa)} casas")
        else:
            recompensa = random.choice([-50,50]) 
            if recompensa > 0:
                toast(f"Parabéns, você chegou na casa surpresa e ganhou {recompensa} de vida")
            else:
                toast(f"Que pena, você chegou na casa surpresa e perdeu {abs(recompensa)} de vida")
        resultado = [decisao, recompensa]
        return resultado

    def casa_da_sorte(self) -> list[int]:
        """ 
        Método que determina o comportamento da casa da sorte. Retorna uma lista de inteiros com o valor 1 no índice 0, indicando que foi um ganho de vida, e o próximo elemento é o valor de vida adquiriada.
        """
        toast(f"Parabéns, você chegou na casa da sorte e ganhou 50 de vida")
        resultado = [1, 50]
        return resultado 
    
    def casa_do_inimigo(self) -> None:
        """ 
        Método que determina o comportamento da casa do inimigo. Retorna a classe 'Monstro', passando como parâmentro o tipo do monstro selecionado aleatoriamente (ogro ou troll), sua força, e sua posição no tabuleiro, nas respectivas casas do inimigo. O monstro só é exibido no tabuleiro com a execução dessa função.
        """
        tipo = random.choice(["ogro", "troll"]) 
        forca = 80 
        x =  self.campo._casas[str(self.numero)]['x'] 
        y = self.campo._casas[str(self.numero)]['y'] 
        inimigo = Monstro(tipo, forca, x, y)
        toast("Oh não! Você encontrou um monstro no caminho, faça de tudo para continuar sua aventura!")
        