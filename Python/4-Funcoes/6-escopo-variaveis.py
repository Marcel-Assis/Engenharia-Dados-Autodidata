# Escopo de variáveis:
# Explicação -> O escopo de uma variável determina onde ela pode ser acessada dentro do código.
# Existem dois tipos principais de escopo: local e global.

# Variável global:
x = 10

def funcao():
    # Variável local:
    y = 5
    print("Dentro da função, x =", x)
    print("Dentro da função, y =", y)

funcao()
print("Fora da função, x =", x)
# print("Fora da função, y =", y)  # Isso causaria um erro, pois y é local à função.

# Variável global pode ser acessada e modificada dentro de funções usando a palavra-chave 'global':
def modificar_global():
    global x
    x = 20

modificar_global()
print("Fora da função, x =", x)  # 20
