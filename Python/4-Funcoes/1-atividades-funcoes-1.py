'''1 - Crie uma função chamada “e_negativo” que receba um número,  
retorna um booleano “True” se o número for negativo, caso contrário 
retorna “False”.'''
def e_negativo(num):
    return num < 0
print(e_negativo(-2))

'''2 - Crie um função que receba um array de números (int ou float) e 
retorne sua soma.'''
def soma_array(arr):
    soma = 0
    for i in arr:
        soma += i
    return soma
array = [10, 50, 40]
print(soma_array(array))

'''3 - Crie um função que receba uma string e que conte e retorne o número 
de vogais desta string.'''
def conta_vogais(texto):
    vogais = 0
    arr_vogais = ('a', 'e', 'i', 'o', 'u')
    for i in texto:
        if i in arr_vogais:
            vogais += 1
    return vogais
print(conta_vogais('Marcel'))

'''4 - Crie um função que retorne o último caractere de um string recebida.'''
def pega_ultimo(texto):
    return texto[-1]
print(pega_ultimo('Marcel'))

'''5 - Crie um função que receba dois números e uma string dizendo se deve 
realizar a soma ou subtração do números.'''
def calculadora(num1, num2, op):
    if op == '+':
        return num1 + num2
    else:
        return num1 - num2 
print(calculadora(4, 2, '+'))