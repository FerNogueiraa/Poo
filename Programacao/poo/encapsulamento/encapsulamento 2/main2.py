from veiculo import Veiculo
from motocicleta import Motocicleta

v = Veiculo("Veiculo", "g34yu5", "Audi", "A3", 2017)
m = Motocicleta("Motocicleta", "asdasd", "Honda", "XJ", 2010, 500)


print(isinstance(v, Veiculo), (v, Motocicleta))
