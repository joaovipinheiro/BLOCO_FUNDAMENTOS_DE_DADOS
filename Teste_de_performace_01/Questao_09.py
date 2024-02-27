valor_compra = float(input("Digite o valor da compra200: "))

if valor_compra > 200:
    desconto = 0.15
elif valor_compra > 100:
    desconto = 0.10
else:
    desconto = 0

valor_final = valor_compra - (valor_compra * desconto)
print("Valor final com desconto: R$", valor_final)
