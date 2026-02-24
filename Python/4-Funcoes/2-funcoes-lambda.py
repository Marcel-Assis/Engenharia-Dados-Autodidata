# Funções lambda (anônimas):
# Como funciona -> lambda parametros: expressão
quadrado = lambda x: x ** 2
print(quadrado(5))  # 25

# Função lambda com múltiplos parâmetros:
soma = lambda a, b: a + b
print(soma(3, 5))  # 8

# Função lambda com condição:
paridade = lambda x: "Par" if x % 2 == 0 else "Ímpar"
print(paridade(4))  # Par
print(paridade(5))  # Ímpar
