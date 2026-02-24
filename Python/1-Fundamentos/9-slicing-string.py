# Slicing:
texto = "Python é incrível!"

# Acessando caracteres individuais
print("Primeiro caractere:", texto[0])
print("Último caractere:", texto[-1])

# Fatiando strings
print("Primeiros 6 caracteres:", texto[:6])
print("Do 7º ao 12º caractere:", texto[6:12])
print("Do 7º caractere até o final:", texto[6:])
print("Do início até o 12º caractere:", texto[:12])
print("Todos os caracteres:", texto[:])

# Operadores de String:
texto = "Programação"
print("a" in texto)
print("z" not in texto)
tamanho = len(texto)
print("Tamanho do texto:", tamanho)