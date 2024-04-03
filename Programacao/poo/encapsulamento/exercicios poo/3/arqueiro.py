from rpg import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome, classe, ataqueEspecial, defesa):
        super().__init__(nome, classe, ataqueEspecial, defesa)


        
C = Arqueiro("Ronaldo", "Arqueiro", "Arco-flecha", "nenhuma")
print(a.__dict__)