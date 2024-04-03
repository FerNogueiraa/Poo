from funcionario import Funcionario

a = Funcionario("Carlos", "Dev", 50)
print(a.__dict__)
a.registrar_hora_trabalhada()
a.registrar_hora_trabalhada()
a.calcular_salario()
print(a.__dict__)

a.salario = 1000

print(a.__dict__)