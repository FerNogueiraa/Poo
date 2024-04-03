eleitores = int(input("Número total de eleitores: "))
branco = int(input("Número de votos em branco: "))
nulo = int(input("Número de votos nulos: "))
valido = int(input("Número de votos válidos:"))

if branco > eleitores:
    print("Inválido")
elif nulo > eleitores:
    print("Inválido")
elif valido > eleitores:
    print("Inválido")


pbranco = (branco * 100) / eleitores
pnulo = (nulo * 100) / eleitores
pvalido = (valido * 100) / eleitores

print(f"A porcentagem de votos em branco é de {pbranco}%")
print(f"A porcentagem de votos nulo é de {pnulo}%")
print(f"A porcentagem de votos válidos são de {pvalido}%")
