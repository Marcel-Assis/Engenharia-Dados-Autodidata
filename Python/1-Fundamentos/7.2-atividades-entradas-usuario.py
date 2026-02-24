'''1 - Crie um programa que leia por
input dois números e realize a divisão
entre ambos. Formate o print para
mostrar o cálculo completo.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = num1 / num2
print(f"{num1} dividido por {num2} é igual a {resultado}")

'''2 - Crie um programa que mostre o dia,
mês, ano, hora, minuto e segundos
inseridos pelo usuário. Formate o
valor.'''

dia = input("Digite o dia: ")
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")
hora = input("Digite a hora: ")
minuto = input("Digite o minuto: ")
segundo = input("Digite o segundo: ")

print(f"Data e hora inseridas: {dia}/{mes}/{ano} {hora}:{minuto}:{segundo}")