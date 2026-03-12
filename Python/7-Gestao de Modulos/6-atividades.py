'''1 - Importe do modulo random a função randrange e crie um programa que gere um único 
número aleatório entre 2 e 100. Em seguida diga se esse número é par ou impar.'''
from random import randrange
numero_aleatorio = randrange(2, 101)
if numero_aleatorio % 2 == 0:
    print(f"O número {numero_aleatorio} é par.")
else:
    print(f"O número {numero_aleatorio} é impar.")

'''2 - Da mesma forma que o exercício anterior, gere a soma de 100 números aleatórios e
mostre o resultado final.'''
soma = 0
for i in range(0, 100):
    soma += randrange(1, 100)
print(soma)

'''3 - Crie um modulo que dispõem de duas funções, uma que subtrai dois números e outra
que soma dois números. Importe essas funções e as use. Não se esqueça de gerar a
documentação destas funções e do modulo e mostrar na saída de seu programa. Chame o
modulo de “calc_python”'''
import calc_python
print(calc_python.subtrai.__doc__)
print(calc_python.subtrai(10, 3))
print(calc_python.soma.__doc__)
print(calc_python.soma(10, 3))

