class Personagem():
    def __init__(self, nome, classe, ataqueEspecial,defesa):
        self.nome = nome
        self.classe = classe
        self.__ataqueEspecial = ataqueEspecial
        self.__defesa = defesa

    @property
    def ataqueEspecial(self):
        return self.__ataqueEspecial

    @property
    def defesa(self):
        return self.__defesa

    @ataqueEspecial.setter
    def ataqueEspecial(self, novoAtaque):
        raise ValueError("Você não pode mudar o valor do ataque do personagem")

    @defesa.setter
    def defesa(self, novaDefesa):
        raise ValueError("Você não pode mudar a defesa do personagem")



