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
for i in randrange(1, 100):
    soma += i
print(soma)