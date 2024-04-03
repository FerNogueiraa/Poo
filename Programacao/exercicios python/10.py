nconta = int(input("Informe o numero da conta: "))
saldo = float(input("Informe o saldo da conta: "))
debito = float(input("Informe o debito:"))
credito = float(input("Informe o crédito:"))

saldoatual = saldo - debito + credito

if saldoatual <= 0:
    print(f"Seu saldo está negativo \n Seu saldo atual é de {saldoatual}")
else:
    print(f"Seu saldo está positivo \n Seu saldo atual é de {saldoatual}")

    
