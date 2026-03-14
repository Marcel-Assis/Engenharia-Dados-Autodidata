# Iteradores em Python
# Um iterador é um objeto que pode ser iterado, ou seja, que pode ser percorrido elemento por elemento. Em Python, os iteradores são usados para percorrer sequências como listas, tuplas, dicionários e conjuntos.
# Criando um iterador a partir de uma lista
minha_lista = [1, 2, 3, 4, 5]
iterador = iter(minha_lista)
# Usando o iterador para percorrer a lista
print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3
print(next(iterador))  # Saída: 4
print(next(iterador))  # Saída: 5
# Se tentarmos chamar next() novamente, obteremos um erro StopIteration, pois o iterador atingiu o final da sequência
try:
    print(next(iterador))
except StopIteration:
    print("O iterador atingiu o final da sequência.")
# Criando um iterador a partir de um dicionário
meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
iterador_dicionario = iter(meu_dicionario)
# Usando o iterador para percorrer as chaves do dicionário
print(next(iterador_dicionario))  # Saída: 'a'
print(next(iterador_dicionario))  # Saída: 'b'
print(next(iterador_dicionario))  # Saída: 'c'
# Criando um iterador a partir de um conjunto
meu_conjunto = {1, 2, 3}
iterador_conjunto = iter(meu_conjunto)
# Usando o iterador para percorrer os elementos do conjunto
print(next(iterador_conjunto))  # Saída: 1 (a ordem pode variar)
print(next(iterador_conjunto))  # Saída: 2 (a ordem pode variar)
print(next(iterador_conjunto))  # Saída: 3 (a ordem pode variar)
# Criando um iterador a partir de uma string
minha_string = "Olá"
iterador_string = iter(minha_string)
# Usando o iterador para percorrer os caracteres da string
print(next(iterador_string))  # Saída: 'O'
print(next(iterador_string))  # Saída: 'l'
print(next(iterador_string))  # Saída: 'á'
