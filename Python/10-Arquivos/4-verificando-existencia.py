from os import path # Importar o módulo os.path para usar a função path.exists() para verificar a existência de arquivos
import os # Importar o módulo os para usar a função os.remove() para deletar arquivos

arquivo_existe = path.exists("Python/10-Arquivos/exemplo.txt") # Verificar se o arquivo "exemplo.txt" existe usando a função path.exists() do módulo os.path. Esta função retorna True se o arquivo existir e False caso contrário.

if arquivo_existe: # Verificar se o arquivo existe
    print("O arquivo existe.") # Imprimir uma mensagem indicando que o arquivo existe
else:
    print("O arquivo não existe.") # Imprimir uma mensagem indicando que o arquivo não existe

# deletando o arquivo para testar novamente
try:
    os.remove("Python/10-Arquivos/exemplo.txt") # Usar a função os.remove() para deletar o arquivo "exemplo.txt". Esta função remove o arquivo especificado do sistema de arquivos. Certifique-se de que o arquivo exista antes de tentar removê-lo para evitar erros. Após a execução desta linha, o arquivo "exemplo.txt" será deletado, e a próxima verificação de existência do arquivo retornará False, indicando que o arquivo não existe mais.
    print('Arquivo deletado com sucesso.') # Imprimir uma mensagem indicando que o arquivo foi deletado com sucesso
except FileNotFoundError: # Capturar a exceção FileNotFoundError caso o arquivo não exista
    print('O arquivo não existe, não é possível deletar.') # Imprimir uma mensagem indicando que o arquivo não existe e não pode ser deletado
finally:
    arquivo = open("Python/10-Arquivos/exemplo.txt", "wt") # O modo "wt" significa "write text", ou seja, escrever em um arquivo de texto. Se o arquivo já existir, ele será sobrescrito. Se o arquivo não existir, ele será criado.
    arquivo.write("Olá, este é um exemplo de arquivo criado em Python.\n") # O método write() é usado para escrever uma string no arquivo. O caractere "\n" é usado para adicionar uma nova linha após o texto.
    arquivo.write("Podemos escrever várias linhas de texto neste arquivo.\n") # Você pode usar o método write() quantas vezes quiser para adicionar mais texto ao arquivo.
    arquivo.close()
    print('Arquivo criado novamente para teste.') # Imprimir uma mensagem indicando que o arquivo foi criado novamente para teste