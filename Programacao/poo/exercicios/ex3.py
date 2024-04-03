class Livro():
    def __init__(self, nomeLivro, qtdPaginas, autor, preco):
        self.nomeLivro = nomeLivro
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco



    def getPreco(self):
        print(self.preco)


    def setPreco(self):
        novoPreco = float(input("DIgite um novo preço para o livro: "))
        self.preco = novoPreco
        print(f"O preço foi alterado para {self.preco}")
    




meuLivro = Livro("O Livro", 150, "Fernandin", 69)
print(meuLivro.__dict__)
meuLivro.getPreco()
meuLivro.setPreco()
meuLivro.getPreco()
print(meuLivro.__dict__)
