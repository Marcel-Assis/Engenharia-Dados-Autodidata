'''1 - Cria um única string que contêm seu nome e
sobrenome, em seguida use o slicing para
separar o nome em uma variável e o seu
sobrenome em outra. Printe esses valores.'''

nome_completo = "Marcel Assis"
nome = nome_completo[:6]
sobrenome = nome_completo[7:]
print("Nome:", nome)
print("Sobrenome:", sobrenome)

'''2 - Leia uma string através do input e retire
o ultimo caractere.'''

string = input("Digite uma string: ")
string_sem_ultimo = string[:-1]
print("String sem o último caractere:", string_sem_ultimo)

'''3 - Faça um programa que leia uma string
através do input e diga se ela possui uma
vogal.'''

string = input("Digite uma string: ")
possui_vogal = ("a" in string) or ("e" in string) or ("i" in string) or ("o" in string) or ("u" in string)
print("A string possui uma vogal?", possui_vogal)

'''4 - Faça um programa que insira a palavra
'ABC' na primeira posição de uma string lida
por input.'''

string = input("Digite uma string: ")
string_com_abc = "ABC" + string[0:]
print("String com 'ABC' no início:", string_com_abc)