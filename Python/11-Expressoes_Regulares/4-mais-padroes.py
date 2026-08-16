# Mais Padrões

import re

# para encontrar todas as ocorrências do mesmo padrão
texto = 'abbabb'
info = re.search('(abb)+', texto) # o padrão dentro do parênteses e o sinal de + busca de 1 até n ocorrências
if info != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')


texto2 = 'aabbaabbbbbbaaccaa'
info2 = re.search('(aa|bb)+', texto2) # o padrão dentro do parênteses e o sinal de + busca de 1 até n ocorrências
if info2 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info2.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info2.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')

texto3 = 'aabbaabbbbbbaaccaa'
info3 = re.search('(aa|bb){2}', texto3) # {2} define que quer apenas as 2 primeiras ocorrencias (aa ou bb)
if info3 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info3.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info3.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')


texto4 = 'abc'
info4 = re.search('(aa|bb)*', texto4) # * mesmo se não encontrar o padrão, não retorna none
if info4 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info4.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info4.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')


texto5 = ''
info5 = re.search('^(aa)?$', texto5) # ? busca de 0 a mais ocorrencias, não retorna none
if info5 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info5.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info5.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')

# definir intervalos de ocorrencia
texto6 = 'aaaaaa'
info6 = re.search('^(aa){2,3}$', texto6) # tem que começar com aa mas que a ocorrencia pode ser de duas ou tres vezes
if info6 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info6.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info6.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')


texto7 = 'xxxxxxx'
# {,7} (7 ou menos)
# {7,} (7 ou mais
info7 = re.search('^x{,7}$', texto7) # se tiver de 0 até 7 x 
if info7 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info7.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info7.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')

# saber se o padrão está presente em qualquer lugar do texto
texto8 = 'Olá sou eu, AQUI, e nada para frente'
info8 = re.search('(.)*(AQUI)(.)*', texto8) # busca o padrão que está no meio dos (.) -> isso indica que pode ter conteúdo entre o padrão pedido
if 8 != None: # se não houver, retorna none, se houver, segue
    print('Encontrado ocorrência em', info8.span()) # exibe em qual índice foi encontrado
    print('O que foi encontrado:', info8.group()) # exibe o que foi encontrado
else:
    print('Nada foi encontrado')