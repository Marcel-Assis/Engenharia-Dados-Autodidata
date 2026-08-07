'''1 - Crie um programa que receba uma string por input e 
conte quantos caracteres ela têm, não leve em conta 
caracteres de espaço. Você não deve usar o len().'''
texto = input("Digite uma string: ")
contador = 0
for caractere in texto:
    if caractere != " ":
        contador += 1
print("A string tem", contador, "caracteres (sem contar espaços).")

'''2 - Crie um programa que faça o calculo do fatorial de um 
número. O fatorial a ser calculado deve ser recebido por 
input.'''
numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print("O fatorial de", numero, "é", fatorial)

'''3 - Crie um programa que leia um quantidade arbitraria 
de textos e concatene eles numa string única.'''
quantidade = int(input("Quantos textos você deseja concatenar? "))
texto_concatenado = ""
for i in range(quantidade):
    texto = input("Digite o texto " + str(i + 1) + ": ")
    texto_concatenado += texto
print("Texto concatenado:", texto_concatenado)

'''4 - Cria um programa que printe a tabuada da divisão de 
um número lido por input.'''
numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero / i
    print(f"{numero} / {i} = {resultado}")

'''5 (DESAFIO) - Crie um programa que percorra os números 
de 3 até 30 e diga o número é primo ou não'''
for num in range(3, 31):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "não é primo")
                break
        else:
            print(num, "é primo")