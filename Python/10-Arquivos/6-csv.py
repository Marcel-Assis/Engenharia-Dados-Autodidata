# Arquivos CSV

# arquivo estruturado em linhas e colunas, onde cada canto é separado por uma vírgula

import csv
# Criando um arquivo csv
with open("pessoas.csv", "w", newline='') as arquivo: # abre/cria o arquivo (w)
    escritorCsv = csv.writer(arquivo, delimiter=',') # cria o objeto escritorCsv, instanciando
    escritorCsv.writerow(['id', 'nome', 'profissão']) # escreve a primeira linha da planilha (nome da coluna)
    escritorCsv.writerow(['1', 'Fernando', 'Eng. de Dados'])
    escritorCsv.writerow(['2', 'Maria', 'Professora'])
    escritorCsv.writerow(['3', 'Rodrigo', 'Dev'])
    escritorCsv.writerow(['4', 'Irene', 'Tec. Informática'])


# Lendo o arquivo
with open('pessoas.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Criando através de uma lista
linhas = [['id', 'nome', 'profissão'],['1', 'Fernando', 'Eng. de Dados'],['2', 'Maria', 'Professora'],['3', 'Rodrigo', 'Dev'],['4', 'Irene', 'Tec. Informática']]
with open('pessoas2.csv', 'w', newline='') as file2:
    escritorCsv = csv.writer(file2) 
    escritorCsv.writerows(linhas) # com writerows ele escreve várias linhas ao mesmo tempo
