palavras = input("Digite algumas palavras separadas por espaço: ").split()

for palavra in palavras:
    if len(palavra) < 5:
        print(palavra, "é uma palavra curta.")
    else:
        print(palavra, "é uma palavra longa.")
