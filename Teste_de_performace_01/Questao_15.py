print("Bem-vindo à aventura!")
print("Você está em uma encruzilhada...")
print("Escolha seu caminho:")
print("1 - Caminho da Floresta")
print("2 - Caminho da Montanha")

escolha = input("Qual caminho você escolhe? ")

if escolha == "1":
    print("Você entrou na floresta...")
    print("Encontrou uma cabana misteriosa!")
    print("Dentro da cabana, você encontra um baú de tesouro!")
else:
    print("Você escalou a montanha...")
    print("No topo, você encontra um dragão adormecido!")
    print("Escolha sua ação:")
    print("1 - Acordar o dragão")
    print("2 - Roubar o tesouro do dragão")

    acao = input("O que você faz? ")

    if acao == "1":
        print("O dragão acorda e... você foge correndo!")
    else:
        print("Você tenta roubar o tesouro, mas o dragão acorda!")
        print("Por sorte, o dragão é amigável e compartilha o tesouro com você!")
