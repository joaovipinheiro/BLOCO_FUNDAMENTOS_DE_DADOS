import random

quantidade = int(input("Quantos dados você quer jogar? "))

for _ in range(quantidade):
    resultado = random.randint(1, 6)
    print("Resultado do dado:", resultado)
