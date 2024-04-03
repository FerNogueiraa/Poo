class Aluno():
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    
    def estudar(self):
        estudar = int(input("Informe quantas horas o aluno está estudando: "))
        self.tempoSemDormir = self.tempoSemDormir + estudar
        print(f"O aluno está {self.tempoSemDormir} horas sem dormir")


    def dormir(self):
        dormir = int(input("Quantas horas de sono o aluno terá: "))
        self.tempoSemDormir = self.tempoSemDormir - dormir
        print(f"No final do dia, o aluno ficou {self.tempoSemDormir} horas sem dormir.")


pessoa = Aluno("Serginho", "Informática", 15)
print(pessoa.__dict__)
pessoa.estudar()
pessoa.dormir()
        