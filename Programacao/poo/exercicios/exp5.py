class Carro():
    def __init__(self, consumo):
        self.combustivel = 0
        self.consumo = consumo

    def adicionarGasolina(self, abastecer):
        self.combustivel += abastecer

    def andar(self, distancia):
        self.combustivel -= distancia/self.consumo
        if(self.combustivel == 0): print("Seu carro parou")

    def obterGasolina(self):
        print(f"Seu nível de combustível é: {self.combustivel}")



meuFusca = Carro(consumo = 15)
meuFusca.adicionarGasolina (abastecer=20)
meuFusca.andar(distancia=100)
meuFusca.obterGasolina()
print(meuFusca.__dict__)