import random

numero_aleatorio = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 100): "))
    
    if palpite == numero_aleatorio:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_aleatorio:
        print("Muito baixo. Tente novamente!")
    else:
        print("Muito alto. Tente novamente!")
