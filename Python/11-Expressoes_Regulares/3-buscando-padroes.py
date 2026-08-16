# Buscando Grupos de Padrões

import re

texto = 'existem 64 predios com 700 metros'
info = re.search('predios', texto) # define o que quer encontrar e atribui na variável info
if info != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')

# [] define que quer encontrar um conjunto
texto2 = 'ABCDefgHI123'
info2 = re.findall('[Ae3]', texto2) # busca A, e, 3
info3 = re.findall('[A-Z]', texto2) # busca A até Z maísculo
info4 = re.findall('[a-z]', texto2) # // minúsculo
info5 = re.findall('[0-9]', texto2) # busca de 0 a 9
info6 = re.findall('[A-Za-z]', texto2) # busca de A até Z e de a até z
print(info2)
print(info3)
print(info4)
print(info5)
print(info6)

# buscar mais de uma informação
info7 = re.findall('predios|metros', texto) # busca duas palavras, | = or, busca um ou outro
print(info7)

info8 = re.findall('[A-Z]|[0-9]', texto2) # | = or
print(info8)

# buscar se tiver no início
info9 = re.search('^existem', texto) # ^ funciona pra procurar a ocorrencia se estiver no início apenas
if info9 != None:
    print('Encontrado ocorrência em', info9.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info9.group()) # exibe o que foi encontrado

# buscar se tiver no final
info10 = re.search('metros$', texto) # $ funciona pra procurar a ocorrencia se estiver no final
if info10 != None:
    print('Encontrado ocorrência em', info10.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info10.group()) # exibe o que foi encontrado

