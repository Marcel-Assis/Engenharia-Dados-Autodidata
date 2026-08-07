# Unpacking de Iteradores


# Percorrer uma lista que contém listas dentro dela
produtos = [
    ['carro', '200.000'],
    ['cadeira', '1000'],
    ['moto', '33000'],
    ['geladeira', '2000'],
    ['armario', '1500']
]

# Usando unpacking não precisou criar dois laços (for dentro de for)
for produto, valor in produtos:
    print(produto, valor)


# Usando unpacking em uma função iterável pra retornar uma lista
def gen1():
    yield [1,2]
    yield [3,4]
    yield [5,6]

for x, y in gen1():
    print(x, y)


# Funções geradoras (Generators) aninhadas
def gen2(): # Primeira função geradora
    yield 1
    yield 2
    yield 3

def gen3(): # Segunda função geradora
    for i in gen2(): # Percorre a primeira função geradora (no caso i = 3 (yields dentro da gen2))
        yield i, 'a'
        yield i, 'b'
        yield i, 'c'
        
print('---')
for x, y in gen3(): # Unpacking delas
    print(x, y)
