# Isto é um comentário de uma linha

'''Isto é
um comentário
de várias linhas'''

# Para exibir algo:
print('Olá mundo!')
print('Maçã', 20, 7.1, True)

# Para exibir algo com separador:
print('Maçã', 'Pêra', 'Uva', sep='-')

# Para exibir algo quebrando linha:
print('Esse é um texto longo\ncom quebra de linha')

# Para exibir algo e incluir um final:
print('Maçã', 'Pêra', 'Uva', end=' Fim\n')

# Para incluir algo ordenado na exibição:
print('A pontuação total de %s foi %s pontos' % ('João', 95))
print('A pontuação total de {} foi {} pontos'.format('Maria', 88))

# Para concatenar:
print('Olá' + ' ' + 'mundo!')

# Para incluir variáveis:
nome = 'Carlos'
idade = 30
print(f'O nome é {nome} e a idade é {idade}')
