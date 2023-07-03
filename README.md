# The-Golden-Way
Jogo de tabuleiro em que dois jogadores escolhem seus respectivos personagens (duende ou fada) do mundo da fantasia e embarcam numa aventura em busca do baú de ouro no final do caminho. Porém, no meio do trajeto eles deverão enfrentar os inimigos (trolls e ogros), acumulando bônus durante o caminho e contando com a sorte nas casas de recompensa surpresa. 

## Regras e Manual de Uso

1. Para executar o jogo basta baixar a pasta e executar no terminal o comando **python main.py**:

![terminal](https://github.com/heleafreitas/The-Golden-Way/assets/82972511/3abd9617-915c-4415-916e-58c66c90ff1b)

2. O primeiro usuário a jogar o dado define a ordem que o jogo vai acontecer. Para isso, deve-se clicar na imagem do dado no canto superior esquerdo da tela e selecionar o método **jogarDado** e **escrever o nome do seu personagem (duende ou fada)**:
   
   2.1. Não será possível jogar o dado duas vezes seguidas, deve-se esperar a vez do oponente na rodada.

![jogarDado](https://github.com/heleafreitas/The-Golden-Way/assets/82972511/7a5b83e1-10b9-47ee-b3b9-5d0f3a78972b)

3. Caso o jogador caia na **casa da sorte**, é acrescentado 50 pontos de vida ao personagem.

4. Caso o jogador caia na **casa surpresa** poderá receber um bônus (ganhar pontos de vida ou avançar até 3 casas) ou uma penalidade (perder pontos de vida ou voltar até 3 casas).

5. Caso o jogador caia na **casa do inimigo** deverá clicar no monstro e selecionar o método **atacar** para tentar sobreviver a ele.

  5.1. Não será possível jogar novamente o dado sem ter enfrentado o inimigo, mesmo que seja a sua rodada.
  
  5.2. Caso sobreviva ao ataque, poderá continuar a jogar mas com uma quantidade de vida menor devido ao ataque sofrido.
  
  5.3. Caso o ponto de vida seja menor que a força do monstro, perderá o embate e retornará ao início da jornada com os pontos de vida iniciais.

![sobreviverInimigo](https://github.com/heleafreitas/The-Golden-Way/assets/82972511/1f9cd8c6-598c-4417-a1b5-9406795d5517)

6. O jogador que chegar primeiro ao final dessa aventura ganha o jogo.

## Visão técnica

É importante detalhar a nossa escolha e intenção sobre quais atributos e métodos manter privados e não permitir que os usuários manipulem. Métodos como ‘verificarVez” que não precisam receber um parâmetro digitado pelo usuário e que atuam para retornar uma informação para o programa, foram ocultados, já que não teriam funcionalidade para os jogadores. Enquanto, métodos como “jogarDados” que precisam receber uma informação do usuário foram mantidos públicos. No âmbitos dos atributos, aqueles que não forneciam uma informação útil para a jogabilidade, como “casas” e “campo” foram omitidos na interface, já aqueles que influenciam o andamento do jogo, como “vida” e “força” permaneceram visíveis para o jogador, mas sem a possibilidade de alterá-los. O mesmo ocorreu para os atributos provenientes do Tupy, como “x”, “y”, “angle” e “file” que também não foram ocultados, mas não podem ser modificados para não obstruir o funcionamento do jogo. Logo, a decisão de privar ou não um método/atributo foi tomada levando em conta a experiência do usuário e visando evitar erros causados por alterações externas. 

## Integrantes

Todos os integrantes participaram da criação de todas as classes, apenas algumas funcionalidades foram feitas separadamente.

Helen Amanda Lima de Freitas (Nota 5) - Readme, método casa da sorte e andar.
Lucas de Araújo Santos Oliveira (Nota 5) - Docstrings, método casa surpresa e verificar casa.
Maria Fernanda Pinto da Fonseca (Nota 5) - Imagens utilizadas, método casa do inimigo e verificar vez


