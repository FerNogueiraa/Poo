nota1 = float(input("Informe a nota da primeira avaliação: "))
nota2 = float(input("Informe a nota da segunda avaliação: "))

mediafinal = (nota1 + nota2) / 2

if mediafinal >= 6:
    print(f"Aprovado!!! \n Sua média final foi de: {mediafinal}")
else:
    print(f"Reprovado!!! \n Sua média final foi: {mediafinal}")