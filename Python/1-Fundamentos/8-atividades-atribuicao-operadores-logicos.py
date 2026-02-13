'''1 - Crie um programa que responda se
você foi aprovado numa prova. Você
somente foi aprovado numa prova se sua
média for maior ou igual que 7 ou se
sua nota no exame for maior ou igual a
5. Leia esses valores por input.'''

media = float(input("Digite sua média: "))
nota_exame = float(input("Digite sua nota no exame: "))

aprovado = media >= 7 or nota_exame >= 5
print('Você foi aprovado?', aprovado)

'''2 - Crie um programa que diga se a
senha esta correta e portanto você tem
acesso ao sistema. A senha devera ser
salva no código, e a tentativa deve
ser lida por input.'''

senha_correta = "123456"
tentativa = input("Digite a senha: ")

acesso = tentativa == senha_correta
print('Acesso ao sistema:', acesso)