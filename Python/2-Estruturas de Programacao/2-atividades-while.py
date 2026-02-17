'''1 - Crie um programa que receba 5 números e retorne a 
média aritmética entre esses números'''
soma = 0
contador = 0
while contador < 5:
    numero = float(input("Digite um número: "))
    soma += numero
    contador += 1
media = soma / 5
print("A média aritmética é:", media)

'''2 - Crie um programa que receba 5 números, realiza a 
soma destes números, mas caso um destes números seja 
negativo não considere ele na soma'''
soma = 0
contador = 0
while contador < 5:
    numero = float(input("Digite um número: "))
    if numero >= 0:
        soma += numero
    contador += 1
print("A soma dos números positivos é:", soma)

'''3 - Cria um programa que receba um número arbitrário 
(definido pelo usuário) de números que serão lidos e 
retorne a soma de todos eles'''
quantidade = int(input("Digite a quantidade de números: "))
soma = 0
contador = 0
while contador < quantidade:
    numero = float(input("Digite um número: "))
    soma += numero
    contador += 1
print("A soma dos números é:", soma)

'''4 - Percorra os números de 2 até 10 e diga se o número é 
par ou impar.'''
numero = 2
while numero <= 10:
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é impar")
    numero += 1

'''5 - Crie um programa que receba como input uma string. 
Em seguida percorra a string e diga quantos espaços em 
branco essa string tem'''
texto = input("Digite uma string: ")
contador_espacos = 0
for caractere in texto:
    if caractere == " ":
        contador_espacos += 1
print("A string tem", contador_espacos, "espaços em branco.")
