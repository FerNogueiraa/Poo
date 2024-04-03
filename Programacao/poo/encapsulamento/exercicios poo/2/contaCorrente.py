from banco import Banco

class ContaCorrente(Banco):
    def __init__(self, nome, senha, email, saldo):
        super().__init__(nome, senha, email, saldo)
        self.__creditoEspecial = 0


    @property
    def creditoEspecial(self):
        return self.__creditoEspecial
    

    @creditoEspecial.setter
    def creditoEspecial(self, a):
        raise ValueError("Deu erro, use o método")
    

    def gerenciamentoCredito(self):
        res = input("Voce deseja realizar um crédito especial? S/N")
        if res.upper() == "S":
            valor = float(input("Digite o valor a ser creditado: "))
            self.__creditoEspecial += valor

        else:
            return