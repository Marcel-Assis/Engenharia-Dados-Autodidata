# Enumerate

# É um método que transforma um objeto iterável em uma tupla com índice e valor :)

lista = ['a', 'b', 'c']
for item in enumerate(lista): # Mostra o índice e o valor da lista
    print(item)


for indice, valor in enumerate(lista): # O python atribui o índice e o valor a uma variável, sem criar tupla
    print(indice, valor)

# Percorrendo uma função com yield e enumerate 
def anos():
    yield '2000'
    yield '2001'
    yield '2002'
    yield '2003'
    yield '2004'
    yield '2005'

for indice, valor in enumerate(anos()):
    print(indice, valor)


# Percorrendo um laço com range e step mostrando o índice com enumerate
for indice, valor in enumerate(range(0, 20, 5)):
    print(indice, valor)