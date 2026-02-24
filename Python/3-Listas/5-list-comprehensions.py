# List Comprehensions:
# Como funciona -> [expressão for item in iterável if condição]
# Exemplo -> [x**2 for x in range(10) if x % 2 == 0]  # Quadrados dos números pares de 0 a 9

# Exemplos:

# Criar uma lista de quadrados:
quadrados = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Aplicar uma função a todos os elementos:
nomes = ["Alice", "Bob", "Charlie"]
nomes_maiusculos = [nome.upper() for nome in nomes]  # ['ALICE', 'BOB', 'CHARLIE']

# List comprehensions aninhadas:
matriz = [[i * j for j in range(5)] for i in range(5)] # Matriz 5x5 com produtos dos índices
for linha in matriz:
    print(linha)

# List comprehensions com condição:
numeros = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# List comprehensions com múltiplas condições:
numeros_filtrados = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]  # [0, 6, 12, 18]

# List comprehensions com else:
numeros_paridade = ["Par" if x % 2 == 0 else "Ímpar" for x in range(10)]  # ['Par', 'Ímpar', 'Par', 'Ímpar', ...]

# Tabuada string formatada:
tabuada_formatada = [f"{i} x {j} = {i * j}" for i in range(1, 11) for j in range(1, 11)]
for linha in tabuada_formatada:
    print(linha)
