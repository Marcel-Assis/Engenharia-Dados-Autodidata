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

'''4 - Cria um modulo para retornar uma lista de números aleatórios. Esse modulo deve
ter a seguinte funcionalidade:
- Uma função que retorna uma lista de números randômicos chamada de
get_random_lista(inicial, final, tam), onde “inicial” é o número mínimo que pode
aparecer na lista e “final” é o número máximo que pode aparecer. Por fim “tam” deve
ser o número de elementos na lista. Chame o modulo de “meu_random”'''
import meu_random
print(meu_random.get_random_lista(1, 100, 10))

'''5 - Crie um programa que tenha a entrada na função e modulo main(). Ele deve receber
dois números via parâmetro do programa e mostrar sua soma. Mas com uma condição:
Verificar se possui dois parâmetros de entrada. Caso contrario parar a execução do
programa e avisar qual o problema.'''
# python -u "/home/marcel/Desktop/Projetos/Engenharia-Dados-Autodidata/Python/7-Gestao de Modulos/teste_programa.py" 10 20