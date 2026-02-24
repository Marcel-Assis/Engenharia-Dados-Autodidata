'''1 - Crie um programa que possui duas variáveis, uma recebe o ano
em que estamos e a outra o ano em que você nasceu. Em seguida
subtraia ambas para receber uma estimativa de quantos anos você
tem. Mostre esse valor na saída do programa.'''
ano_atual = 2026
ano_nascimento = 1993
idade = ano_atual - ano_nascimento
print('Você tem aproximadamente', idade, 'anos.')

'''2 - Crie um programa que faz a média aritmética entre três
números. Estes números devem ser salvos em uma variável. Mostre
esse valor na saída do programa.'''
num1 = 5
num2 = 10
num3 = 15
media = (num1 + num2 + num3) / 3
print('A média aritmética é', media)

'''3 - Crie um programa que calcule o IMC (índice de massa corporal).
O IMC é dado pelo peso em KG divido pela altura em metros elevado
ao quadrado. Salvar esses valores em uma variável. Mostre esse
valor na saída do programa.'''
peso = 70
altura = 1.75
imc = peso / (altura ** 2)
print('O IMC é', imc)

'''4 (Desafio) - Você tem um determinado números de ovos de páscoa
para dividir entre um determinado número de pessoas (duas
variáveis iniciais). Determine quantos ovos ficarão por pessoa e
quantos ovos sobrarão pois não puderam ser divido igualmente.
Lembre o número de ovos por pessoa é um número inteiro'''
ovos = 20
pessoas = 6
ovos_por_pessoa = ovos // pessoas
ovos_sobrando = ovos % pessoas
print('Cada pessoa receberá', ovos_por_pessoa, 'ovos.')
print('Sobraram', ovos_sobrando, 'ovos.')