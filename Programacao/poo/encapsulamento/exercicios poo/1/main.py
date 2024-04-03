from programador import Programador
from gerente import Gerente


#Programador
b = Programador("joao", "Programador", 0, 8, 10, 0)
print(f"O {b.cargo} {b.nome} tem {b.salario} de salario, contando com {b.bonus} de bonus")

b.calcularSalario()
print(f"O {b.cargo} {b.nome} tem {b.salario} de salario, contando com {b.bonus} de bonus")

b.calcularBonus()
print(f"O {b.cargo} {b.nome} tem {b.salario} de salario, contando com {b.bonus} de bonus")


#Gerente
a = Gerente("Pedro", "Gerente", 0, 5, 20, 0)
print(f"O {a.cargo} {a.nome} tem {a.salario} de salario, contando com {a.bonus} de bonus")

a.calcularSalario()
print(f"O {a.cargo} {a.nome} tem {a.salario} de salario, contando com {a.bonus} de bonus")

a.calcularBonus()
print(f"O {a.cargo} {a.nome} tem {a.salario} de salario, contando com {a.bonus} de bonus")