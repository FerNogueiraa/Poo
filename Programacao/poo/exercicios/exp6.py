class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self) -> str:
        return self.nome
    
    class Equipe:
        def __init__(self, participantes, projeto):
            self.participantes = participantes
            self.projeto = projeto


    def __str__(self):
        participantes_nomes = ", ".join(str(Aluno) for aluno in self.participantes)
        return f"Projeto: {self.projeto}, Participantes: {participantes_nomes}"
    
    class GerenciadorEquipes:
        def __init__(self, equipes=None):
            if equipes is None:
                self.equipes = []
            else:
                self.equipes = equipes

        def criarEquipe(self,participantes,projeto):
            for equipe in self.equipes:
                if equipe.projeto == projeto:
                    for aluno in equipe.participantes:
                        if aluno in participantes:
                            return "A qeuipe não pode ser criada."
            
            nova_equipe = Equipe(participantes, projeto)
            self.equipes.append(nova_equipe)
            return "A equipe foi criada com sucesso."
        
#Cria um gerenciador de equipes
gerenciador = GerenciadorEquipes()

#Cria 9 alunos
alunos = [Aluno(f"Aluno {i+1}", f"CPF {i+1}") for i in range (9)]

#Cria 3 equipes com 3 alunos cada um e num projeto por equipe

for i in range(3):
    participantes = alunos[i*3:(i+1)*3] #Pega 3 alunos para cada equipe
    projeto = f"Projeto {i+1}" #Cria um projeto para cada equipe
    resultado = gerenciador.criarEquipe(participantes, projeto)
    print(resultado) #Deve imprimir: "A equipe foi criada com sucesso." para cada equipe

    for equipe in gerenciador.equipes:
        print(equipe)


        