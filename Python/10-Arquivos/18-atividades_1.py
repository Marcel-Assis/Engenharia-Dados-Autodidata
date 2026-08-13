# Atividades Parte I

'''1 - Leia o seguinte arquivo (“exercicio1.txt”) e transforme em uma lista'''
print("Atividade 1")
lista = []
with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/FormacaoPython/Download/11.Ler_e_escrever_Arquivos/exercicio1.txt', 'rt') as arquivo:
    for item in arquivo:
        lista.append(item.strip()) # strip retira os /n do final

print(lista)

'''2 - Leia o seguinte arquivo (“exercicio2.txt”), onde cada linha tem um produto e seu valor. Crie uma classe chamada Produto, para representar cada item do arquivo, com nome e valor. Salve todos produtos em uma lista, ao final imprima a lista item por item, mostrando nome e valor.'''
print('\nAtividade 2')
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

produtos = []

with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/FormacaoPython/Download/11.Ler_e_escrever_Arquivos/exercicio2.txt', 'rt') as arquivo:
    for linha in arquivo:
        indice_separa = linha.index("R$")
        nome = linha[:indice_separa-1]
        valor = linha[indice_separa:len(linha)-1]
        produto = Produto(nome, valor)
        produtos.append(produto)

for produto in produtos:
    print(produto.nome, produto.valor)

'''3 - Escreva num arquivo os números de 0 até 100. Uma linha para cada número.'''
with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio3.txt', 'wt') as arquivo:
    for i in range(0, 101):
        arquivo.write(str(i) + '\n')

'''4 - Escreva num arquivo todos números positivos e menores que 100 que são divisíveis por 3.'''
with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio4.txt', 'wt') as arquivo:
    for i in range(0, 101):
        if (i % 3 == 0):
            arquivo.write(str(i) + '\n')

'''5 - Crie um arquivo CSV separado por virgula para guardar informações de sua família. Nesse arquivo deve constar em cada linha o nome de um membro da família e o grau de parentesco(Ex: pai). Escreva 5 membros da família no arquivo. Faça uma função que ira escrever no arquivo, e outra que ira ler o arquivo.'''
print('\nAtividade 5')
import csv
with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio5.csv', 'w', newline='') as arquivo:
    escritorCsv = csv.writer(arquivo, delimiter=',')
    escritorCsv.writerow(['nome', 'parentesco']) # escreve a primeira linha da planilha (nome da coluna)
    escritorCsv.writerow(['Fernando', 'Pai'])
    escritorCsv.writerow(['Maria', 'Mãe'])
    escritorCsv.writerow(['Rodrigo', 'Irmão'])
    escritorCsv.writerow(['Irene', 'Irmã'])
    escritorCsv.writerow(['Oliver', 'Primo'])

def escrever_csv(nome, parentesco):
    with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio5.csv', 'a', newline='') as arquivo:
        escritorCsv = csv.writer(arquivo, delimiter=',')
        escritorCsv.writerow([nome, parentesco])

def ler_csv():
    with open('C:/Users/marce/Projetos/Engenharia-Dados-Autodidata/Python/10-Arquivos/exercicio5.csv', 'r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            print(row)

escrever_csv('Marcelo', 'Avô')
escrever_csv('Luis', 'Tio')

ler_csv()