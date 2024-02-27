import random

personagens = ["um mago", "um pirata", "um astronauta"]
acoes = ["descobriu um portal", "encontrou um tesouro", "fez amizade com um dragão"]
locais = ["na floresta", "no fundo do mar", "na lua"]

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

historia = f"{personagem} {acao} {local}."
print(historia)
