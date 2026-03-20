# Lendo arquivos em Python
# Para ler um arquivo em Python, você pode usar a função `open()`, que retorna um objeto de arquivo. Você pode usar o método `read()` para ler o conteúdo do arquivo como uma string, ou o método `readlines()` para ler o conteúdo do arquivo como uma lista de linhas. Aqui está um exemplo de como ler um arquivo em Python:
# Abrir o arquivo para leitura
arquivo = open("Python/10-Arquivos/exemplo2_with.txt", "rt") # Abrir o arquivo para leitura
conteudo = arquivo.read() # Ler o conteúdo do arquivo
print(conteudo) # Imprimir o conteúdo do arquivo
arquivo.close() # Fechar o arquivo

# Usar a declaração with para abrir o arquivo e garantir que ele seja fechado automaticamente
with open("Python/10-Arquivos/exemplo2_with.txt", "rt") as arquivo: # Abrir o arquivo para leitura usando a declaração with
    conteudo = arquivo.read() # Ler o conteúdo do arquivo
    print(conteudo) # Imprimir o conteúdo do arquivo
# Neste exemplo, o arquivo será fechado automaticamente após a execução do bloco with, mesmo que ocorra um erro durante a leitura.

# Ler o arquivo linha por linha usando um loop for
with open("Python/10-Arquivos/exemplo2_with.txt", "rt") as arquivo: # Abrir o arquivo para leitura
    for linha in arquivo: # Iterar sobre cada linha do arquivo
        print(linha.strip()) # Imprimir a linha, removendo espaços em branco extras

# Ler o arquivo usando o método readlines()
with open("Python/10-Arquivos/exemplo2_with.txt", "rt") as arquivo: # Abrir o arquivo para leitura
    linhas = arquivo.readlines() # Ler todas as linhas do arquivo em uma lista
    print(linhas) # Imprimir a lista de linhas
# Neste exemplo, o método readlines() lê todas as linhas do arquivo e as armazena em uma lista chamada linhas, que é então impressa. Cada elemento da lista representa uma linha do arquivo, incluindo o caractere de nova linha (\n) no final de cada linha.

# Ler o arquivo usando o método readline()
arquivo = open("Python/10-Arquivos/exemplo2_with.txt", "rt") # Abrir o arquivo para leitura
primeira_linha = arquivo.readline() # Ler a primeira linha do arquivo
print(primeira_linha) # Imprimir a primeira linha do arquivo
segunda_linha = arquivo.readline() # Ler a segunda linha do arquivo
print(segunda_linha) # Imprimir a segunda linha do arquivo
arquivo.close() # Fechar o arquivo

# Ler o arquivo usando um loop while e o método readline()
arquivo = open("Python/10-Arquivos/exemplo2_with.txt", "rt") # Abrir o arquivo para leitura
while True: # Loop infinito para ler o arquivo linha por linha
    linha = arquivo.readline() # Ler uma linha do arquivo
    if not linha: # Verificar se a linha está vazia (fim do arquivo)
        break # Sair do loop se for o fim do arquivo
    print(linha.strip()) # Imprimir a linha, removendo espaços em branco extras
arquivo.close() # Fechar o arquivo

# Ler o arquivo usando um loop for diretamente no objeto de arquivo
with open("Python/10-Arquivos/exemplo2_with.txt", "rt") as arquivo: # Abrir o arquivo para leitura
    for linha in arquivo: # Iterar sobre cada linha do arquivo
        print(linha)
# O arquivo será fechado automaticamente ao sair do bloco with