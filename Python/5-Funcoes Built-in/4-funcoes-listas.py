# Funções para manipulação de listas:

lista = [1, 2, 3, 4, 5]

# Adição de elementos:
lista.append(6)  # [1, 2, 3, 4, 5, 6]
lista.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]

# Remoção de elementos:
lista.remove(3)  # [0, 1, 2, 4, 5, 6]
lista.pop()  # [0, 1, 2, 4, 5]

# Ordenação de listas:
lista.sort()  # [0, 1, 2, 4, 5]
lista.sort(reverse=True)  # [5, 4, 2, 1, 0]
# sort por tamanho
texto = ["aaaa", "bbb", "cc", "d"]
texto.sort(key=len)  # Isso ordenaria a lista de strings pelo tamanho das palavras
print(texto)  # ['d', 'cc', 'bbb', 'aaaa']

# Inversão de listas:
lista.reverse()  # [0, 1, 2, 4, 5]

# Contagem de elementos:
print(lista.count(2))  # 1

# Localização de elementos:
print(lista.index(4))  # 3

# Comprimento da lista:
print(len(lista))  # 5

# Iteração sobre elementos:
for elemento in lista:
    print(elemento)

# Verificação de presença de elemento:
print(3 in lista)  # False

# Verificação de ausência de elemento:
print(3 not in lista)  # True

# Limpeza da lista:
lista.clear()  # []

# Verificação de lista vazia:
print(len(lista) == 0)  # True

# Criação de dicionário a partir de chaves:
d = dict.fromkeys(["a", "b", "c"], 10)
print(d)  # {'a': 10, 'b': 10, 'c': 10}