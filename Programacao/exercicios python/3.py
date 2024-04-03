vcarro = float(input("Escreva o valor do carro: "))

idistri = (vcarro * 28) / 100
imposto = (vcarro * 45) / 100

valorfinal = vcarro + imposto + idistri

print(f"O valor final do carro para o consumidor vai ser de R${valorfinal}")