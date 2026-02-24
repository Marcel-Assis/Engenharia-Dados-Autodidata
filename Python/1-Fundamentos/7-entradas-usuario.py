# Entrada do usuário:

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Olá, %s! Você tem %d anos." % (nome, idade))

# Entrada do usuário com casting:

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

print("Sua altura é %.2f metros e seu peso é %.2f kg." % (altura, peso))