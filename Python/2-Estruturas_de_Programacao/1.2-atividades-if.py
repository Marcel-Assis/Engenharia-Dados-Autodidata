'''1 - Crie um programa que receba o seu saldo bancário e o quanto
você deve. Em seguida o programa deve dizer se você tem saldo
positivo ou negativo.'''
saldo = float(input("Digite o seu saldo bancário: "))
divida = float(input("Digite o valor da sua dívida: "))
if saldo > divida:
    print("Você tem saldo positivo.")
elif saldo < divida:
    print("Você tem saldo negativo.")
else:
    print("Você tem saldo neutro.")

'''2 - Crie um programa que possui uma variável que guarde seu CPF
e que guarde uma senha de sua escolha. Em seguida receba por
input uma senha do usuário. Caso a senha recebida seja a correta
mostre o CPF, caso não diga que a senha esta incorreta.'''
cpf = "123.456.789-00"
senha = "senha123"
senha_input = input("Digite a sua senha: ")
if senha_input == senha:
    print("Seu CPF é:", cpf)
else:
    print("Senha incorreta.")

'''3 - Crie um programa que fale sobre sua idade. As regras são a
seguinte, você deve receber por input sua idade, se você tiver ate
três anos printe que é um bebe, ate 13 anos uma criança, ate 18
anos adolescente, até 65 adulto. Em nenhum deste casos é um
idoso'''
idade = int(input("Digite a sua idade: "))
if idade <= 3:
    print("Você é um bebê.")
elif idade <= 13:
    print("Você é uma criança.")
elif idade <= 18:
    print("Você é um adolescente.")
elif idade <= 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

'''4 - Crie um programa que receba dois números, e também receba
do usuário a operação que deve ser feita, as possibilidades são
soma(+), subtração (-), divisão(/) e multiplicação(*). Realize a
operação escolhida sobre os dois números.'''
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)