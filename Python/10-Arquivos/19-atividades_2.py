# Atividades Parte II

'''6 - Faça um programa que leia um arquivo CSV separado por virgula “exercicio6.csv”, onde cada linha tem os seguintes valores (id_empresa, nome_empresa, numero_funcionarios, lucro). Modele uma classe empresa que será usada para guardar os valores do arquivo. Imprima o resultado. '''
print('Atividade 6')
import csv
with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio6.csv', 'w', newline='') as arquivo:
    escritorCsv = csv.writer(arquivo, delimiter=',')
    escritorCsv.writerow(['id_empresa', 'nome_empresa', 'numero_funcionarios', 'lucro']) # escreve a primeira linha da planilha (nome da coluna)

class Empresa:
    def __init__(self, id_empresa, nome_empresa, numero_funcionarios, lucro):
        self.id_empresa = id_empresa
        self.nome_empresa = nome_empresa
        self.numero_funcionarios = numero_funcionarios
        self.lucro = lucro
    @staticmethod
    def guarda_valores(*empresas):
        with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio6.csv', 'w', newline='') as arquivo:
            escritorCsv = csv.writer(arquivo, delimiter=',')
            for empresa in empresas:
                escritorCsv.writerow([empresa.id_empresa, empresa.nome_empresa, empresa.numero_funcionarios, empresa.lucro])
coluna = Empresa('id_empresa', 'nome_empresa', 'numero_funcionarios', 'lucro')
empresa1 = Empresa('1', 'Marabraz', '8000', 110.090)
empresa2 = Empresa('2', 'Americanas', '4000', 11.090)
empresa3 = Empresa('3', 'Icomon', '8000', 180.090)
Empresa.guarda_valores(coluna, empresa1, empresa2, empresa3)

with open ('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio6.csv', 'r', newline='') as arquivo:
    reader = csv.reader(arquivo)
    for row in reader:
        print(row)

'''7 - Crie uma classe que represente uma pessoa, com nome e idade. Após criar pelo menos 3 instâncias da classe, crie um método que transforme essas instâncias em um dicionário, para pode-las salvar em um arquivo em formato JSON, com nome de “exercicio7.json”. Este método devem ser um tipo estático da classe. Leia o arquivo depois de salvo.'''
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @staticmethod
    def salva_pessoas(*pessoas):
        dict = None
        for pessoa in pessoas:
            dict = pessoa
        return dict
pessoa1 = Pessoa('Marcel', '32')
pessoa2 = Pessoa('Ana', '31')
Pessoa.salva_pessoas(pessoa1, pessoa2)


'''8 - Com base no exercício anterior, agora crie uma função do tipo da classe que leia o arquivo gerado e retorne as instâncias de classes de volta em uma lista.'''


'''9 - Crie um arquivo XML, nesse arquivo XML haverá a tag raiz Root. Dentro dessa raiz podem haver varias tags Estado com atributo nome. Dentro de cada estado pode haver a tag Cidade mas nesse caso o valor da tag (texto) devera ser o nome da cidade. Crie um programa que gere esse arquivo com alguns estados e municípios.'''

