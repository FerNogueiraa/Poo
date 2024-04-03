from contaCorrente import ContaCorrente
from contaPP import contaPP

CC = ContaCorrente("joao", 123, "joão@gmail.com", 1000)
print(CC.__dict__)

CC.deposito(100)
print(CC.__dict__)

CC.sacar(300)
print(CC.__dict__)
