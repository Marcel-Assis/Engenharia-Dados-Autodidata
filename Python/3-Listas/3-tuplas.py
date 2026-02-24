# Tuplas:

# Criar uma tupla:
minha_tupla = (1, 2, 3, 4, 5)

# Acessar elementos da tupla:
print(minha_tupla[0])  # Primeiro elemento
print(minha_tupla[-1])  # Último elemento

# Tuplas são imutáveis, então não é possível adicionar, remover ou alterar elementos
# minha_tupla[0] = 10  # Isso geraria um erro

# Operações com tuplas:
outra_tupla = (4, 5, 6, 7, 8)
concatenacao = minha_tupla + outra_tupla  # Concatenação
repeticao = minha_tupla * 2  # Repetição
posicao = minha_tupla.index(4)  # Retorna a posição do elemento 4
contar = minha_tupla.count(4)  # Conta quantas vezes o elemento 4 aparece na tupla

# Verificar se um elemento está na tupla:
existe = 4 in minha_tupla  # True

# Atribuir valores da tupla em variáveis:
a, b, c, d, e = minha_tupla  # Atribui os valores da tupla às variáveis a, b, c, d & e

# Casting:
lista = list(minha_tupla)  # Converte a tupla em lista
lista[0] = 10  # Altera o primeiro elemento da lista
lista.append(6)  # Adiciona um elemento no final da lista
minha_tupla = tuple(lista)  # Converte a lista de volta para tupla