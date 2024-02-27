print("Escolha a operação:")
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")

escolha = input("Digite a operação quer deseja realizar: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = num1 + num2
    if resultado.is_integer():
        resultado = int(resultado)
    print("Resultado da adição:", resultado)
    
elif escolha == '2':
    resultado = num1 - num2
    if resultado.is_integer():
        resultado = int(resultado)
    print("Resultado da subtração:", resultado)
    
elif escolha == '3':
    resultado = num1 * num2

    if resultado.is_integer():
        resultado = int(resultado)
    print("Resultado da multiplicação:", resultado)
elif escolha == '4':

    if num2 != 0:
        resultado = num1 / num2
        if resultado.is_integer():
            resultado = int(resultado)
        print("Resultado da divisão:", resultado)
    else:
        print("Não é possível dividir por zero!")
else:
    print("Escolha inválida. Por favor, escolha 1, 2, 3 ou 4 para a operação.")
