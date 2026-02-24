# Funções recursivas:
# Explicação -> Uma função recursiva é uma função que chama a si mesma para resolver um problema.
# É importante definir uma condição de parada para evitar loops infinitos.

# Função recursiva para calcular o fatorial de um número:
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # 120

# Função recursiva para calcular a soma dos números de 1 até n:
def soma_numeros(n):
    if n == 0:
        return 0
    else:
        return n + soma_numeros(n - 1)

print(soma_numeros(5))  # 15

# Função recursiva para calcular o n-ésimo número da sequência de Fibonacci:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # 5

# Função recursiva para calcular o máximo divisor comum (MDC) de dois números:
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

print(mdc(48, 18))  # 6

# Função recursiva para calcular a potência de um número:
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

print(potencia(2, 3))  # 8

# Função recursiva para calcular a soma dos dígitos de um número:
def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma_digitos(n // 10)

print(soma_digitos(123))  # 6