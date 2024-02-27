frase = input("Digite uma palavra ou frase para verificar se é um palíndromo: ").lower()
frase_sem_espaco = frase.replace(" ", "")

if frase_sem_espaco == frase_sem_espaco[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
