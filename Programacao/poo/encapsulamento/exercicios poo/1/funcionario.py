
class Funcionario():
    def __init__(self, nome, cargo, salario, horas, val_hora, bonus):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario
        self.horas = horas
        self.bonus = bonus
        self.val_hora = val_hora
    
        

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, a):
        raise ValueError("Você não pode alterar o valor do salário")

    def calcularSalario(self):
        dia = int(input("Quantos dias foram trabalhados?"))
        self.__salario = (self.val_hora * self.horas) * dia
    
    def calcularBonus(self):
        qnt = float(input("Qual será o valor do bonus?"))
        self.__salario += qnt
        self.bonus = qnt
