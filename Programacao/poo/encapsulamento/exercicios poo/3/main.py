from guerreiro import Guerreiro
from mago import Mago
from arqueiro import Arqueiro




a = Guerreiro("João", "Guerreiro", "Espada", "Escudo")
print(a.__dict__)

b = Mago("Pedrinho", "Mago", "Cajado", "Escudo De chakra")
print(b.__dict__)

C = Arqueiro("Ronaldo", "Arqueiro", "Arco-flecha", "nenhuma")
print(C.__dict__)