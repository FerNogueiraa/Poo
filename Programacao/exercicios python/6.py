maca = 0

comprar = int(input("Informe quantas maçãs deseja comprar: "))

if comprar >= 12:
    maca = 1
else:
    maca = 1.30

valorfinal = comprar * maca

print(f"O preço final das maçãs é de {valorfinal}")
