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