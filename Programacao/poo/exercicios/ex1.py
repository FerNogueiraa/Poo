class Triangulo():
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def calcularPerimentro(self):
        print(self.ladoA + self.ladoB + self.ladoC)
    
    def getMaiorLado(self):
        print(max(self.ladoA, self.ladoB, self.ladoC))
    
    def mostrarArea(self):
        print((self.ladoC * self.ladoB) /2)

a= int(input("Digite o valor de lado A: "))
b= int(input("Digite o valor de lado B: "))
c= int(input("Digite o valor de lado C: "))

meuTriangulo = Triangulo(a, b, c)
meuTriangulo.calcularPerimentro()
meuTriangulo.getMaiorLado()
meuTriangulo.mostrarArea()
