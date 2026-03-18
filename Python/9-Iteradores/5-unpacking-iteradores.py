# Unpacking de interadores é uma técnica que permite extrair os elementos de um iterador e atribuí-los a variáveis de forma concisa. Isso é especialmente útil quando você tem um iterador que retorna múltiplos valores, como uma tupla ou uma lista, e deseja atribuir esses valores a variáveis individuais.

produtos = [
    ["Produto A", 10.99, 5],
    ["Produto B", 15.49, 3],
    ["Produto C", 7.99, 8]
]

for nome, preco, quantidade in produtos:
    print(f"Nome: {nome}, Preço: {preco}, Quantidade: {quantidade}")

# No exemplo acima, temos uma lista de produtos, onde cada produto é representado por uma lista contendo o nome, o preço e a quantidade. Usando o unpacking de iteradores, podemos extrair esses valores diretamente na declaração do loop for, atribuindo-os a variáveis nome, preco e quantidade. Isso torna o código mais legível e conciso.

# O unpacking de iteradores também pode ser usado com outras estruturas de dados, como dicionários. Por exemplo, se tivermos um dicionário de produtos, podemos usar o método items() para obter os pares chave-valor e fazer o unpacking diretamente:
produtos_dict = {
    "Produto A": (10.99, 5),
    "Produto B": (15.49, 3),
    "Produto C": (7.99, 8)
}

for nome, (preco, quantidade) in produtos_dict.items():
    print(f"Nome: {nome}, Preço: {preco}, Quantidade: {quantidade}")
# Neste exemplo, o método items() retorna um iterador de pares chave-valor, onde a chave é o nome do produto e o valor é uma tupla contendo o preço e a quantidade. Usando o unpacking de iteradores, podemos extrair esses valores diretamente na declaração do loop for, tornando o código mais limpo e fácil de entender.

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    for i in gen1():
        yield i, 'a'
        yield i, 'b'
        yield i, 'c'

for x, y in gen2():
    print(f"x: {x}, y: {y}")
# Neste exemplo, temos duas funções geradoras, gen1 e gen2. A função gen1 gera os números 1, 2 e 3, enquanto a função gen2 itera sobre os valores gerados por gen1 e, para cada valor, gera uma tupla contendo o valor e uma letra. Usando o unpacking de iteradores, podemos extrair os valores diretamente na declaração do loop for, atribuindo-os às variáveis x e y. Isso torna o código mais legível e fácil de entender, especialmente quando lidamos com iteradores que retornam múltiplos valores.