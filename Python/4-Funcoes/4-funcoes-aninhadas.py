# Funções aninhadas (ou funções internas):
# Explicação -> Uma função aninhada é uma função definida dentro de outra função.
# Elas são úteis para organizar o código e encapsular funcionalidades que não precisam ser acessíveis fora da função principal.

def saudacao(nome):
    def mensagem():
        return f"Olá, {nome}!"
    return mensagem()

print(saudacao("Alice"))  # Olá, Alice!

# Função aninhada para calcular o quadrado de um número:
def calcular_quadrado(numero):
    def quadrado():
        return numero ** 2
    return quadrado()

print(calcular_quadrado(4))  # 16

# Função aninhada para calcular o cubo de um número:
def calcular_cubo(numero):
    def cubo():
        return numero ** 3
    return cubo()

print(calcular_cubo(2))  # 8