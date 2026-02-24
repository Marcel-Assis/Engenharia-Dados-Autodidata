# Funções:
# Como definir -> def nome_da_funcao(parametros):
# Exemplo -> def saudacao(nome): return f"Olá, {nome}!"

# Exemplos:

# Função simples:
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Alice"))  # Olá, Alice!

# Função com múltiplos parâmetros:
def soma(a, b):
    return a + b

print(soma(3, 5))  # 8

# Função com valor padrão:
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(3))  # 9
print(potencia(3, 3))  # 27

# Função com retorno múltiplo:
def coordenadas():
    return 10, 20

x, y = coordenadas()
print(x, y)  # 10 20

# Função com argumentos variáveis:
def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4))  # 10

# Função com argumentos nomeados variáveis:
def imprimir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_info(nome="Alice", idade=25, cidade="São Paulo")

# Função com argumentos posicionais e nomeados:
def exemplo_funcao(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

exemplo_funcao(1, 2, 3, 4, nome="Alice", idade=25)

