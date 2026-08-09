# Criando Primeiros Arquivos

arquivo = open("exemplo.txt", "wt") # atribui a variável pro arquivo exemplo.txt, se não existir, ele é criado
arquivo.write("Olá estou escrevendo no arquivo\n")
arquivo.write("Esta é a segunda linha do arquivo")
arquivo.close()

# Quebra de linha
lista = ["Ana", "Fernando", "João", "Maria"]
arquivo2 = open("nomes.txt", "wt") # wt = se o arquivo não existir, vai criar
for i in lista:
    arquivo2.write(i + '\n')
arquivo2.close()

# Writelines
texto = "Ana\nFernando\nJoão\nMaria"
arquivo3 = open("nomes2.txt", "wt")
arquivo3.writelines(texto) # escreve a linha inteira
arquivo3.close()

# Ternário
lista = [str(i) + '\n' for i in range(0,20)]
arquivo4 = open("numeros.txt", "wt")
arquivo4.writelines(lista)
arquivo4.close()