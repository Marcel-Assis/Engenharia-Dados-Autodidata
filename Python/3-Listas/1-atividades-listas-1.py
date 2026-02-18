'''1 - Crie uma lista com os seguintes números 1,10,6,7,8,10. Em seguida printe a
soma destes números.'''
numeros = (1, 10, 6, 7, 8, 10)
soma = 0
for numero in numeros:
    soma += numero
print(f"A soma é: {soma}")

'''2 - Cria uma lista e preencha ela com valores de 1 a 100. Em seguida printe esses
valores.'''
numeros = []
for x in range(1, 101):
    numeros.append(x)
print(numeros)

'''3 - Crie duas listas com os seguintes valores 30,4,43,52,65,-10 e
43,2,4,76,32,65,3. Agora faça a junção dessas listas, mas se houverem valores
repetidos entre ambas eles não podem repetir na lista unida.'''
lista1 = {30, 4, 43, 52, 65, -10}
lista2 = {43, 2, 4, 76, 32, 65, 3}
juncao_listas = lista1.union(lista2)
print(juncao_listas)

'''4 - Crie uma lista contendo o nome de todos os meses do ano. Em seguida receba
por input o mês (número) em que você nasceu e mostre qual o nome do mês que
você nasceu.'''
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
input_mes = int(input("Digite o número do mês que você nasceu: "))
print(lista_meses[input_mes - 1])

'''- Crie uma lista contendo todos dias (número) do mês em que você nasceu. Em
seguida receba por input o dia (número) em que você nasceu e remova desta
lista. Ao final mostre o conteúdo da lista.'''
lista_dias_setembro = []
for dia in range(1, 31):
    lista_dias_setembro.append(dia)
input_dia = int(input("Digite o dia do mês em que você nasceu: "))
lista_dias_setembro.remove(input_dia)
print(lista_dias_setembro)