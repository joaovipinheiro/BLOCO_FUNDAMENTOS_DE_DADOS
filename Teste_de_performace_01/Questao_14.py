votos = {"Opção 1": 0, "Opção 2": 0, "Opção 3": 0}

while True:
    print("Escolha uma opção para votar:")
    for opcao in votos:
        print(opcao)

    escolha = input("Digite sua escolha (ou 'sair' para encerrar): ")

    if escolha.lower() == "sair":
        break
    elif escolha in votos:
        votos[escolha] += 1
        print("Voto computado!")
    else:
        print("Opção inválida. Tente novamente.")

print("Resultado da votação:")
for opcao, votos_num in votos.items():
    print(opcao + ":", votos_num)
