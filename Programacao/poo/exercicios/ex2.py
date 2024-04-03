class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario 

    def aumentarSalario(self, salario):
        porcentagem = int(input(f"Seu salário é de {salario}\n Quantos porcento queres aumentar?"))
        aumento = (porcentagem * salario) / 100
        salarioFinal = aumento + salario
        print(f"Seu salário atual é de {salarioFinal}")
        return salarioFinal


nome = str(input("De um nome ao funcionário: "))
salario = int(input("Informe o salário: "))

meuSalario = Funcionario(nome, salario)
meuSalario.aumentarSalario(salario)

