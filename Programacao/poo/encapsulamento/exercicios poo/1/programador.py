from funcionario import Funcionario

class Programador(Funcionario):
   def __init__(self, nome, cargo, salario, horas, val_hora, bonus):
        super().__init__(nome, cargo, salario, horas, val_hora, bonus)
      


