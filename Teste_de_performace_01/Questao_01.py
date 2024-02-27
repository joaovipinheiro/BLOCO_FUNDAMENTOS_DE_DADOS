# Pedindo ao usuário para inserir dois números
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# Verificando se os números são inteiros ou decimais
if '.' in num1 or '.' in num2:
    num1 = float(num1)
    num2 = float(num2)
else:
    num1 = int(num1)
    num2 = int(num2)

# Calculando e exibindo a soma, subtração, multiplicação, divisão e divisão inteira
print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Divisão:", num1 / num2)
print("Divisão Inteira:", num1 // num2)
