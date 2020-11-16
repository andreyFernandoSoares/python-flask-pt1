import csv
from jogo import Jogo

def le_jogos():
    jogos = []
    with open("jogo.csv") as arquivo:
        dados = csv.reader(arquivo)

        for linha in dados:
            nome, categoria, console = linha
            jogo = Jogo(nome, categoria, console)
            jogos.append(jogo)
    
    return jogos
