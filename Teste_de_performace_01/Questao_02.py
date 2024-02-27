minutos = int(input("Digite a quantidade de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print("Horas:", horas)
print("Minutos:", minutos_restantes)

horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

minutos_total = horas * 60 + minutos
print("Total em minutos:", minutos_total)
