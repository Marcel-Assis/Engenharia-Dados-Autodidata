# Criando e Excluindo Pastas

import os
# mkdir cria uma pasta
# rmdir remove uma pasta
caminho_relativo = 'nova_pasta' # define o nome da pasta
try: # criei uma lógica que cada vez que roda, cria ou apaga a pasta, dependendo do erro de existência
    os.mkdir(caminho_relativo) # cria e define o nome da pasta
    print("Pasta", caminho_relativo, "criada")
except:
    os.rmdir(caminho_relativo) # remove a pasta, que deve estar vazia
    print("Pasta", caminho_relativo, "apagada")

caminho_absoluto = 'Python/10-Arquivos/pasta' # define o nome da pasta
try: # criei uma lógica que cada vez que roda, cria ou apaga a pasta, dependendo do erro de existência
    os.mkdir(caminho_absoluto) # cria e define o nome da pasta
    print("Pasta criada em", caminho_absoluto)
except:
    os.rmdir(caminho_absoluto) # remove a pasta, que deve estar vazia
    print("Pasta apagada")

# Criar pasta dentro de pasta
os.mkdir("Python/10-Arquivos/pasta1") # cria a primeira pasta
os.mkdir("Python/10-Arquivos/pasta1/pasta2") # cria a segunda pasta

os.rmdir("Python/10-Arquivos/pasta1/pasta2") # remove a segunda pasta primeiro
os.rmdir("Python/10-Arquivos/pasta1") # remove a primeira pasta (que agora está vazia)


# Criação em lote de pastas + txt

# Criar pasta e depois arquivo
for i in range(0, 10):
    nome_pasta = 'pasta' + str(i)
    try:
        os.mkdir(nome_pasta)
        print(nome_pasta, "criada")
    except Exception as erro:
        print(erro)
        pass
    try:
        open(nome_pasta + '/texto.txt', 'wt').close()
    except Exception as erro:
        print(erro)
        pass

# Apagar arquivo e depois pastas
for i in range(0, 10):
    nome_pasta = 'pasta' + str(i)
    try:
        os.remove(nome_pasta + '/texto.txt')
        print("Arquivo removido")
    except Exception as erro:
        print(erro)
        pass

    try:
        os.rmdir(nome_pasta)
        print(nome_pasta, "removida")
    except:
        print("Falha ao excluir a pasta", nome_pasta)

# Excluir pastas mesmo com arquivos dentro
import shutil
for i in range(0,10):
    nome_pasta = 'pasta' + str(i)

    try:
        shutil.rmtree(nome_pasta)
        print(nome_pasta, "e arquivos removidos através do shutil")
    except:
        print("Falha ao excluir a pasta", nome_pasta)

# Listar conteúdo
files = os.listdir() # lista o conteúdo do diretório aberto
print(files)

files2 = os.listdir("Python/10-Arquivos") # lista o conteúdo da pasta específica
print(files2)