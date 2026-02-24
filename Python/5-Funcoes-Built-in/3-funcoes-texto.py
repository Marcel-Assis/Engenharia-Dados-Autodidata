# Funções para manipulação de texto:

texto = "Olá, Mundo!"

# Maiúsculas e minúsculas:
print(texto.upper())  # "OLÁ, MUNDO!"
print(texto.lower())  # "olá, mundo!"
print(texto.swapcase())  # "oLÁ, mUNDO!"
print(texto.title())  # "Olá, Mundo!"

# Centralização de texto:
print(texto.center(20, "-"))  # "----Olá, Mundo!----"

# Justificação de texto:
print(texto.ljust(20, "-"))  # "Olá, Mundo!--------"
print(texto.rjust(20, "-"))  # "--------Olá, Mundo!"

# Remoção de espaços em branco:
print(texto.strip())  # "Olá, Mundo!"

# Substituição de caracteres:
print(texto.replace("Mundo", "Python"))  # "Olá, Python!"

# Divisão e junção de strings:
print(texto.split(","))  # ["Olá", " Mundo!"]
print(" ".join(["Olá", "Python!"]))  # "Olá Python!"
texto2 = "Olá\nMundo!\nEste é um teste"
print(texto2.splitlines())  # ["Olá", "Mundo!", "Este é um teste"]

# Verificação de presença de substring:
print("Mundo" in texto)  # True

# Contagem de ocorrências de uma substring:
print(texto.count("o"))  # 2

# Localização de uma substring:
print(texto.find("Mundo"))  # 5

# Localização de uma substring (lança erro se não encontrar):
print(texto.index("Mundo"))  # 5

# Verificação de início e fim de string:
print(texto.startswith("Olá"))  # True
print(texto.endswith("Mundo!"))  # True

# Comprimento da string:
print(len(texto))  # 12

# Acesso a caracteres individuais:
print(texto[0])  # "O"
print(texto[-1])  # "!"

# Fatiamento de strings:
print(texto[0:4])  # "Olá,"
print(texto[5:])  # "Mundo!"

# Iteração sobre caracteres:
for char in texto:
    print(char)

# Verificação de caracteres alfabéticos:
print(texto.isalpha())  # False

# Verificação de caracteres numéricos:
print(texto.isdigit())  # False

# Verificação de caracteres alfanuméricos:
print(texto.isalnum())  # False

# Verificação de caracteres em branco:
print(texto.isspace())  # False

# Verificação de caracteres em maiúsculas:
print(texto.isupper())  # False

# Verificação de caracteres em minúsculas:
print(texto.islower())  # False

# Verificação de caracteres em título:
print(texto.istitle())  # True

# Verificação de caracteres decimais:
print(texto.isdecimal())  # False

