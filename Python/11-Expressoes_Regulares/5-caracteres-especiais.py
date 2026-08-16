# Caracteres Especiais

import re

texto = '01234 ABC'

info = re.search('\d+', texto) #\d quer dizer qualquer número, \d+ vai mostrar o intervalo da ocorrencia

if info != None:
    print('Encontrada ocorrência em', info.span())
    print('O que foi encontrado:', info.group())

texto2 = '01234 ABC'

info2 = re.search('\D+', texto2) #\D+ vai buscar a NÃO ocorrência no padrão (no caso não vai mostrar numeros), 

if info2 != None:
    print('Encontrada ocorrência em', info2.span())
    print('O que foi encontrado:', info2.group())

texto3 = '01234 ABC'

info3 = re.search('\s', texto3) # \s vai buscar os espaços em branco, \S vai buscar a não ocorrencia

if info3 != None:
    print('Encontrada ocorrência em', info3.span())
    print('O que foi encontrado:', info3.group())


texto4 = '01234 ABC'

info4 = re.search('\w', texto4) #\w qualquer tipo de caractere numérico ou texto, \W detecta a ausência dos mesmos

if info4 != None:
    print('Encontrada ocorrência em', info4.span())
    print('O que foi encontrado:', info4.group())