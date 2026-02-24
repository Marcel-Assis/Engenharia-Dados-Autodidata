'''6 - Crie um função que receba uma lista de elementos e um valor qualquer. Em 
seguida retorne um booleano dizendo se o valor foi encontrado ou não na lista.'''
def encontrar_valor(arr, valor):
    if valor in arr:
        return True
    return False
array1 = [1, '3', True, 'Olá', 7.1]
print(encontrar_valor(array1, 3))

'''7 - Crie um função que receba uma lista de elementos e um valor qualquer.  Em 
seguida retorne um booleano dizendo se o valor foi encontrado ou não e também 
a posição onde foi encontrado.'''
def encontra_posicao(arr, valor):
    for i in range(0, len(arr)):
        if (arr[i] == valor):
            return True, i
    return False, -1
array2 = [1, 2, 3, 4, 5]
print(encontra_posicao(array2, 6))

'''8 - Crie uma função que recebe um número arbitrário de parâmetros. Em seguida 
diga qual o tipo de cada parâmetro'''
def tipos_param(*args):
    for i in args:
        print(type(i))
tipos_param(1, '2', True, 7.1)

'''9 - Crie uma função que receba um string, mas que possua um decorator para 
transforma-la em uma citação, ou seja você deve retornar strings entre aspas 
duplas, além disso transforme todos os caracteres para minúscula usando a 
função lower()'''
def citacao(func):
    def inner_func(texto):
        return '"' + func(texto).lower() + '"'
    return inner_func

@citacao
def transforma(texto):
    return texto

print("E disse João:", transforma("SÓ OS SÁBIOS SABEM!"))

'''10 - Cria uma função recursiva que itere os números de 0 até 10 e printe o 
resultado de sua divisão inteira com o número três'''
def printa_div_3(num):
    print(f'{num} x 3 = {num // 3}')
    if num >= 10:
        return
    printa_div_3(num + 1)

printa_div_3(0)