from rpg import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, classe, ataqueEspecial, defesa):
        super().__init__(nome, classe, ataqueEspecial, defesa)


        
a = Guerreiro("João", "Guerreiro", "Espada", "Escudo")
print(a.__dict__)