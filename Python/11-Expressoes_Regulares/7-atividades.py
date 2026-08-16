import re

'''1 - Faça uma expressão regular para reconhecer números de 20 até 35 apenas. O texto deve ser composto apenas destes números, nenhum outro caractere é permitido'''
texto1 = '30'
info1 = re.search('^([2][0-9])|([3][0-5])$', texto1)
if info1 != None:
    print('Padrão válido', info1.group())
else:
    print('Padrão inválido')

'''2 - Faça uma expressão regular para dizer se a palavra 'python' esta na frase.'''
texto2 = 'python está na frase'
info2 = re.search('python', texto2)
if info2 != None:
    print('Padrão válido', info2.group())
else:
    print('Padrão inválido')


'''3 - Faça uma expressão regular para validar se uma string dada é um dia da semana. As possibilidades são:
Segunda-Feira
Terça-Feira
Quarta-Feira
Quinta-Feira
Sexta-Feira
Sábado
Domingo'''

texto3 = 'Segunda-Feira'
info3 = re.search('^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$', texto3)
if info3 != None:
    print('Padrão válido', info3.group())
else:
    print('Padrão inválido')

'''4 - Faça uma expressão regular para detectar telefones que comecem com 95. Telefones que começam com 95 devem ser bloqueados. Um número de telefone deve ser válido para poder ser validado, na forma XXXXXXXX onde X é um número. Primeiro diga se é um número válido. Caso seja diga se ele foi bloqueado ou não.'''
texto4 = '95999999'
info4 = re.search('^([0-9]{8})', texto4)
if info4 != None:
    print('Padrão válido', info4.group())
    info42 = re.search('^95([0-9]{6})$', texto4)
    if info42 != None:
        print('Bloqueado')
    else:
        print('Não bloqueado')
else:
    print('Padrão inválido')

'''5 - Faça uma expressão regular para reconhecer palavrados no gerúndio. Normalmente essas palavras podem ser detectadas caso elas terminem com ando, endo, indo: Exemplo: sorrindo, andando. Usa a função “find all” para retornar as ocorrências.'''
texto5 = 'Eu não estou dormindo, estou acordando para sair correndo'
info5 = re.findall('([\w]+ando|[\w]+endo|[\w]+indo)', texto5)
if info5 != None:
    print('Padrão válido', info5)
else:
    print('Padrão inválido')
'''6 - Faça um expressão regular para detectar se a hora é válida: O formato é de 24 horas, e é especificado da seguinte forma: HH:MM
Ex:
19:30
09:30
23:45
23:70 (invalido)'''
texto6 = '19:30'
info6 = re.search('^([0-1][0-9]|[2][0-3]):[0-5][0-9]$', texto6)
if info6 != None:
    print('Padrão válido', info6.group())
else:
    print('Padrão inválido')

'''7 (DESAFIO) - Faça uma expressão regular para validar se uma expressão é uma conta 
matemática valida. Nessa conta matemática só podem haver 2 números inteiros sendo 
somados ou subtraídos entre si. Valide se é uma expressão matemática ou não.'''
texto7 = '201+ 5584 '
info7 = re.search('^ *(\d+ *(-|\+) *\d+) *$', texto7)
if info7 != None:
    print('Padrão válido', info7.group())
else:
    print('Padrão inválido')