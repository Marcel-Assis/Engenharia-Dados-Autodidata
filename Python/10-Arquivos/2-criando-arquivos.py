# Criando um arquivo de texto
arquivo = open("exemplo.txt", "wt") # O modo "wt" significa "write text", ou seja, escrever em um arquivo de texto. Se o arquivo já existir, ele será sobrescrito. Se o arquivo não existir, ele será criado.
arquivo.write("Olá, este é um exemplo de arquivo criado em Python.\n") # O método write() é usado para escrever uma string no arquivo. O caractere "\n" é usado para adicionar uma nova linha após o texto.
arquivo.write("Podemos escrever várias linhas de texto neste arquivo.\n") # Você pode usar o método write() quantas vezes quiser para adicionar mais texto ao arquivo.
arquivo.close() # É importante lembrar de fechar o arquivo após a escrita para garantir que os dados sejam salvos corretamente e liberar os recursos do sistema. Você também pode usar a declaração with para garantir que o arquivo seja fechado automaticamente, mesmo que ocorra um erro durante a escrita.

# Criando um arquivo a partir de uma lista
lista = ["Ana", "Bruno", "Carla", "Diego"] # Suponha que você tenha uma lista de nomes e queira criar um arquivo de texto onde cada nome esteja em uma linha separada. Você pode usar um loop para iterar sobre a lista e escrever cada nome no arquivo, adicionando um caractere de nova linha ("\n") após cada nome para garantir que eles fiquem em linhas separadas.
arquivo = open("nomes.txt", "wt") # Abrir o arquivo para escrita
for i in lista: # Iterar sobre cada elemento da lista
    arquivo.write(i + "\n") # Escrever o elemento no arquivo seguido de um caractere de nova linha
arquivo.close()

# Criando um arquivo a partir de uma string
texto = "Ana\nBruno\nCarla\nDiego" # Se você tiver uma string onde cada linha de texto está separada por um caractere de nova linha ("\n"), você pode usar o método writelines() para escrever a string no arquivo. O método writelines() espera uma sequência de strings, então você pode passar a string diretamente, e ela será escrita no arquivo como está, com as quebras de linha incluídas.
arquivo = open("nomes2.txt", "wt")
arquivo.writelines(texto)
arquivo.close()

# Criando um arquivo a partir de uma lista usando list comprehension
lista = [str(i) + "\n" for i in range(1, 11)] # Se você tiver uma lista de números e quiser criar um arquivo de texto onde cada número esteja em uma linha separada, você pode usar uma list comprehension para criar uma nova lista de strings, onde cada número é convertido para string e seguido por um caractere de nova linha ("\n"). Em seguida, você pode usar o método writelines() para escrever a lista de strings no arquivo.
arquivo = open("numeros3.txt", "wt")
arquivo.writelines(lista)
arquivo.close()

# Criando um arquivo usando a declaração with
# Usar a declaração with para criar um arquivo é uma prática recomendada, pois garante que o arquivo seja fechado automaticamente após a execução do bloco, mesmo que ocorra um erro durante a escrita. Aqui está um exemplo de como criar um arquivo usando a declaração with:
with open("exemplo2_with.txt", "wt") as arquivo: # Abrir o arquivo para escrita usando a declaração with
    arquivo.write("Este é um exemplo de arquivo criado usando a declaração with.\n") # Escrever uma linha de texto no arquivo
    arquivo.write("A declaração with garante que o arquivo seja fechado automaticamente.\n") # Escrever outra linha de texto no arquivo
# Neste exemplo, o arquivo "exemplo2_with.txt" será criado e as duas linhas de texto serão escritas nele. Após a execução do bloco with, o arquivo será fechado automaticamente, mesmo que ocorra um erro durante a escrita. Isso torna o código mais seguro e fácil de ler, além de garantir que os recursos do sistema sejam liberados corretamente.