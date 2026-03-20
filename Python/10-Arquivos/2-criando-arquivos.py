# Criando um arquivo de texto
arquivo = open("exemplo.txt", "wt")
arquivo.write("Olá, este é um exemplo de arquivo criado em Python.\n")
arquivo.write("Podemos escrever várias linhas de texto neste arquivo.\n")
arquivo.close()

# Criando um arquivo a partir de uma lista
lista = ["Ana", "Bruno", "Carla", "Diego"]
arquivo = open("nomes.txt", "wt")
for i in lista:
    arquivo.write(i + "\n")
arquivo.close()

# Criando um arquivo a partir de uma string
texto = "Ana\nBruno\nCarla\nDiego"
arquivo = open("nomes2.txt", "wt")
arquivo.writelines(texto)
arquivo.close()

# Criando um arquivo a partir de uma lista usando list comprehension
lista = [str(i) + "\n" for i in range(1, 11)]
arquivo = open("numeros3.txt", "wt")
arquivo.writelines(lista)
arquivo.close()