# Exemplos Práticos

import re

# validar temperatura
texto = '-10 Cº'

info = re.search('^(-)?[0-9]+ Cº$', texto) # deve começar (^) com o -, mas - é opcional ter (?), depois espera números de 0 a 9 ([0-9]) e pode ter mais de um numero de 0 a 9 (+), e deve terminar com Cº ($)
if info != None:
    print('Encontrada ocorrência em', info.span())
    print('O que foi encontrado', info.group())
    print('Temperatura válida')
else:
    print('Temperatura inválida')


# validar numero de telefone
# regra: deve começar com 99 e deve ter exatamente 8 dígitos e ser somente números
texto2 = '99224466'
info2 = re.search('^99([0-9]{6})', texto2) # deve começar com 99 (^), deve ter numeros de 0-9 e ter exatamente 8 dígitos ({6}) -> nesse caso são 99 do começo + 6
if info2 != None:
    print('Encontrada ocorrência em', info2.span())
    print('O que foi encontrado', info2.group())
    print('Número válido')
else:
    print('Número inválido')


# detectar se uma frase possui exatamente duas palavras
# pode ter espaço no meio e no final
texto3 = 'Texto      teste        '
info3 = re.search('(^[A-Za-z]+ +[A-Za-z]+ *$)', texto3)
if info3 != None:
    print('--Padrão encontrado')
    print('Encontrada ocorrência em', info3.span())
    print('O que foi encontrado:', info3.group())
else:
    print('Padrão não encontrado')

# validar a entrada de uma data
# DD/MM/AAAA
# O dia pode variar de 00 a 31
# O mês de 00 a 12
# O ano de 0000 a 9999
texto4 = '30/11/1998'
info4 = re.search('^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$', texto4)
if info4 != None:
    print('--Padrão encontrado')
    print('Encontrada ocorrência em', info4.span())
    print('O que foi encontrado:', info4.group())
else:
    print('Padrão não encontrado')