while True:
    while True:
        nota1 = int(input("Digite a primeira nota: "))
        if nota1 >  10 or nota1 < 0:
            print("Digite valores de 0 a 10 apenas")
        else:
            break

    while True:
        nota2 = int(input("Digite a segunda nota: "))
        if nota2 >  10 or nota2 < 0:
            print("Digite valores de 0 a 10 apenas")
        else:
            break

    mediafinal = (nota1 + nota2) / 2

    print(f"Media final:{mediafinal}")
    continuar = input("Deseja continuar? (S/N)\n")
    if continuar == "N":
        break
    elif continuar == "n":
        break