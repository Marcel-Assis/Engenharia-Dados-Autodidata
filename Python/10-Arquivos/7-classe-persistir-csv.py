# Criando uma Classe Pessoa Persistindo em CSV
import csv
class Pessoa:
    def __init__(self, id, nome, profissao):
        self.id = id
        self.nome = nome
        self.profissao = profissao

    @staticmethod # método estático pra otimizar os recursos, sem precisar usar a cada instância
    def le_pessoas():
        pessoas = [] # inicializa a lista vazia
        with open('pessoas.csv', 'r') as arquivo: # abre arquivo pessoas com r (ja deve existir)
            leitor = csv.reader(arquivo, delimiter=',') # cria o objeto leitor (reader)
            for linha in leitor: # percorre as linhas do leitor (arquivo que foi aberto)
                pessoa = Pessoa(linha[0], linha[1], linha[2]) # instancia a classe Pessoa na variável pessoa, e atribui às propriedades id, nome, profissão
                pessoas.append(pessoa) # insere na lista as informações da variável pessoa (id, nome, profissão)
        return pessoas

    @staticmethod # método estático pra otimizar os recursos, sem precisar usar a cada instância
    def salva_pessoas(*pessoas): # usa o *pessoas porque >pode< salvar várias instancias/objetos da classe Pessoa ao mesmo tempo, número arbitrário de argumentos 
        with open('pessoas.csv', 'w', newline='') as arquivo:
            escritorCsv = csv.writer(arquivo, delimiter=',')
            for pessoa in pessoas: # pessoas é o número arbitrário de parâmetros que recebeu
                escritorCsv.writerow([pessoa.id, pessoa.nome, pessoa.profissao]) # escreve no arquivo csv as informações/propriedades de uma pessoa de cada vez

# instanciar a classe
coluna = Pessoa('id', 'nome', 'profissão') # opcional
pessoa1 = Pessoa(23, 'José', 'Engenheiro')
pessoa2 = Pessoa(12, 'Maria', 'Arquiteta')
pessoa3 = Pessoa(44, 'Ana', 'Cientista de Dados')

# como tem método estático, não utiliza pessoa.método, utiliza Pessoa.métodoestático

Pessoa.salva_pessoas(coluna, pessoa1, pessoa2, pessoa3) # com método estático + passando os objetos como argumentos (arbitrários do salva_pessoa)
# pessoa1.salva_pessoas() # se não tivesse método estático

lista_pessoa = Pessoa.le_pessoas() # acessando o método estático através da classe diretamente

# percorre
for pessoa in lista_pessoa:
    print(pessoa.id, pessoa.nome, pessoa.profissao)