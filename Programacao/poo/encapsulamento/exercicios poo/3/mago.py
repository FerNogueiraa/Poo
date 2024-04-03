from rpg import Personagem

class Mago(Personagem):
    def __init__(self, nome, classe, ataqueEspecial, defesa):
        super().__init__(nome, classe, ataqueEspecial, defesa)


        
b = Mago("Pedrinho", "Mago", "Cajado", "Escudo De chakra")
print(a.__dict__)