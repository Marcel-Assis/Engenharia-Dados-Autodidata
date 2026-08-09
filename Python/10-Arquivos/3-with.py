# With
# Uma forma mais elegante de abrir e fechar o arquivo (automaticamente)

with open("exemplo_with.txt", "wt") as arquivo:
    arquivo.write("Olá estou escrevendo no arquivo\n")
    arquivo.write("Esta é a segunda linha do arquivo")


print('\n# Ler arquivo já criado')
arquivo = open("exemplo.txt", "rt") # rt lê em modo texto
lido = arquivo.read() # atribui o conteúdo do arquivo na variável
print(lido)
arquivo.close()

print('\n# Ler um pedaço do arquivo')
arquivo = open("exemplo.txt", "rt") # rt lê em modo texto
lido = arquivo.read(10) # atribui as 10 primeiras posições do conteúdo do arquivo na variável
print(lido)
arquivo.close()

# Ler linha por linha
print("\n# Ler linha por linha")
arquivo = open("exemplo.txt", "rt") # rt lê em modo texto
primeira_linha = arquivo.readline()
segunda_linha = arquivo.readline()
print(primeira_linha)
print(segunda_linha)
arquivo.close()

# Percorrer arquivo
print("\n# Percorrer arquivo")
arquivo = open("exemplo.txt", "rt") # rt lê em modo texto
for linha in arquivo:
    print(linha)
arquivo.close()

# Percorrer com for + with
print("\n# Percorrer com for + with")
with open("exemplo.txt", "rt") as arquivo:
    for linha in arquivo:
        print(linha)

