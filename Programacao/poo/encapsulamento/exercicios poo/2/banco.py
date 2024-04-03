class Banco():
    def __init__(self, nome, senha, email, saldo):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    

    @saldo.setter
    def saldo(self):
        raise ValueError("Use os métodos depositar ou debitar para alterar o valor")
    

    def sacar(self, saque):
        self.__saldo -= saque
        print("Seu novo saldoo: ", self.__saldo)

    def deposito(self, deposito):
        self.__saldo += deposito
        print("Seu novo saldo: ", self.saldo)
