import math
'''1 - Crie uma função que retorne a subtração de dois elementos, mas que
considere o valor absoluto deste valores.'''
def absoluto(num1, num2):
    return abs((num1 - num2))
print(absoluto(0, -6))

'''2 - Sem usar “ifs”, crie uma função que receba dois números e retorne a
soma dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser
sempre maior que 0.'''
def somaSemIf(num1, num2):
    soma = num1 + num2
    soma = min(10000, soma)
    soma = max(0, soma)
    return soma
print(somaSemIf(5000, 6000))

'''3 (DESAFIO) - Crie uma função que receba argumentos de tamanho arbitrário.
Todos esses argumentos serão números. Em seguida retorne o menor número
entre todos os recebidos.'''
def menorNumero(*numeros):
    lista_numeros = numeros
    return min(lista_numeros)

print(menorNumero(5, 2, 3))

'''4 - Crie uma função que calcule a formula de Bhaskara, encontrando o X. Os
coeficientes a,b e c devem ser lidos por input.'''
# def bhaskara():
#     a = float(input("Informe a: "))
#     b = float(input("Informe b: "))
#     c = float(input("Informe c: "))
#     delta = (b ** 2) - (4 * a) * c
#     x1 = (-b + math.sqrt(delta)) / (2 * a)
#     x2 = (-b - math.sqrt(delta)) / (2 * a)
#     return x1, x2
# print(bhaskara())

'''5 - Crie uma função que receba uma string, e para cada letra minúscula a
transforme em uma letra maiúscula e vice versa.'''
def conversorString(texto):
    return texto.swapcase()
print(conversorString('Marcel Assis'))