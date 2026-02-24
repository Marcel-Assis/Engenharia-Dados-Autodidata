# Formas de criar listas:
minha_lista = [1, 2, 3, 4, 5]
outra_lista = list(range(1, 6))

# Acessando listas:
print(minha_lista[0])  # Primeiro elemento
print(minha_lista[-1])  # Último elemento
print(outra_lista[2])  # Terceiro elemento

# Operações com lista:
minha_lista.append(6)  # Adiciona um elemento no final
minha_lista.remove(3)  # Remove o elemento 3
minha_lista.insert(2, 10)  # Insere o elemento 10 na posição 2
minha_lista.pop()  # Remove o último elemento
#minha_lista.clear()  # Remove todos os elementos
contar = minha_lista.count(10)  # Conta quantas vezes o elemento 10 aparece na lista
posicao = minha_lista.index(2)  # Retorna a posição do elemento 10 na lista

# Juntar listas:
lista_concatenada = minha_lista + outra_lista  # Concatena duas listas

# Multiplicar listas:
lista_multiplicada = minha_lista * 2  # Multiplica a lista por 2

# Atribuir valores da lista em variáveis:
a, b, c, d, e = minha_lista  # Atribui os valores da lista às variáveis a, b, c, d & e

# Percorrer uma lista com for:
for elemento in minha_lista:
    print(elemento)  # Exibe cada elemento da lista

# Percorrer uma lista com while:
i = 0
while i < len(minha_lista):
    print(minha_lista[i])
    i += 1

# Separar listas de dentro de uma lista:
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
primeira_lista = lista[0]
segunda_lista = lista[1]
terceira_lista = lista[2]

# Acessar lista dentro de lista:
elemento = lista[0][1]  # Acessa o segundo elemento da primeira lista