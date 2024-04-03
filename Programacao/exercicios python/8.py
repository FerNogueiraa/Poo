anoatual = int(input("Informe o ano atual: "))
anonascimento = int(input("Informe o ano de seu nascimento:"))
if (anoatual - anonascimento >= 18):
    print("Você pode votar!!!")
else:
    print("Você ainda não pode votar")