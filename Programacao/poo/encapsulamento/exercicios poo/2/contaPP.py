from banco import Banco

class contaPP(Banco):
    def __init__(self, nome, senha, email, saldo):
        super().__init__(nome, senha, email, saldo)
        

    def calcularJuros(self):
        meses = int(input("Digite o tanto de meses: "))
        valorJuros = self.saldo * meses * (5/100)
        self.deposito(valorJuros)
