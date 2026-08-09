# Verificando Existência e Tratando Erros

# Path
from os import path # verificar se o arquivo existe
arquivo_existe = path.exists("exemplo.txt") # caminho relativo do arquivo (está no mesmo diretório onde o programa está rodando)

if arquivo_existe: # se True
    print("o arquivo existe")
else: # se False
    print("O aquivo não existe")

# Caminho absoluto
teste_arquivo = path.exists("Python/10-Arquivos/3-with.py") # caminho absoluto do arquivo
if teste_arquivo:
    print("Existe")
else:
    print("Não existe")

# Excluir arquivo
import os
try:
    os.remove("<Nome do arquivo>")
except Exception as error:
    print("Ocorreu um erro:", error)

# Se ocorrer uma exceção ou não, o finally garante que haja o fechamento do arquivo
file = open("teste", "w") # cria o arquivo (w -> abre um arquivo para escrita, se não existir, cria)
try:
    file.write("hello world") # tenta escrever nele
finally:
    file.close() # fecha independente se houver erro ou não