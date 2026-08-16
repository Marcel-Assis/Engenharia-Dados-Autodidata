# Exemplos Básicos

import re # importa o regex

texto = '001234510'
info = re.search('1', texto) # define o que quer encontrar e atribui na variável info
if info != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')

# encontrar todas as ocorrências
info2 = re.findall('1', texto) # findall retorna uma lista com todas as ocorrencias
print('findall', info2)

# dividir a string e transformar em lista o que não for pedido
info3 = re.split('1', texto) # o split divide a string antes e depois do encontrado, sem mostrar o que foi pedido
print('split', info3)

# substituir um caractere por outro
info4 = re.sub('1', '#', texto) # sub substitui o 1 por #
print('sub', info4)