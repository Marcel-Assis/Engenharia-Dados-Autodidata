import csv
class Pessoa:
    def __init__(self, id, nome, profissao):
        self.id = id
        self.nome = nome
        self.profissao = profissao
    @staticmethod
    def le_pessoas():
        pessoas = []
        with open("pessoas.csv", "r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=",")
            for linha in leitor:
                pessoa = Pessoa(linha[0], linha[1], linha[2])
                pessoas.append(pessoa)
            return pessoas
    @staticmethod
    def salva_pessoas(*pessoas):
        with open("pessoas.csv", "w") as arquivo:
            escritor = csv.writer(arquivo, delimiter=",")
            for pessoa in pessoas:
                escritor.writerow([pessoa.id, pessoa.nome, pessoa.profissao])
            print("Pessoas salvas com sucesso.")
        
pessoa1 = Pessoa(1, "João", "Engenheiro")
pessoa2 = Pessoa(2, "Maria", "Médica")
pessoa3 = Pessoa(3, "Pedro", "Professor")

Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3)

lista_pessoa = Pessoa.le_pessoas()
for pessoa in lista_pessoa:
    print(f"ID: {pessoa.id}, Nome: {pessoa.nome}, Profissão: {pessoa.profissao}")