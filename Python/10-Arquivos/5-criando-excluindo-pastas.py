# Criando e excluindo pastas em Python
import os # Importar o módulo os para usar a função os.mkdir() para criar pastas e a função os.rmdir() para deletar pastas

try:
    os.rmdir("Python/10-Arquivos/nova_pasta") # Usar a função os.rmdir() para deletar a pasta "nova_pasta" que foi criada anteriormente. Esta função remove um diretório vazio do sistema de arquivos. Certifique-se de que a pasta esteja vazia antes de tentar removê-la, caso contrário, ocorrerá um erro. Após a execução desta linha, a pasta "nova_pasta" será deletada do sistema de arquivos.
    print('Pasta deletada com sucesso.') # Imprimir uma mensagem indicando que a pasta foi deletada com sucesso
except FileNotFoundError: # Capturar a exceção FileNotFoundError caso a pasta não exista
    print('A pasta não existe, não é possível deletar.') # Imprimir uma mensagem indicando que a pasta não existe e não pode ser deletada
finally:
    os.mkdir("Python/10-Arquivos/nova_pasta") # Usar a função os.mkdir() para criar uma nova pasta chamada "nova_pasta" dentro do diretório "Python/10-Arquivos". Esta função cria um novo diretório no sistema de arquivos com o nome especificado. Certifique-se de que o caminho para a nova pasta seja válido e que você tenha permissões adequadas para criar pastas no local especificado.
    print('Pasta criada com sucesso.') # Imprimir uma mensagem indicando que a pasta foi criada com sucesso


######

# Criando várias pastas com arquivos txt dentro de cada uma
for i in range(0, 10):
    nome_pasta = 'pasta' + str(i)
    try:
        os.mkdir(nome_pasta)
        print('Pasta', nome_pasta, 'criada com sucesso.') # Imprimir uma mensagem indicando que a pasta foi criada com sucesso
    except:
        pass
    
    try:
        open(nome_pasta + '/texto.txt', 'wt').close()
        print('Arquivo texto.txt criado com sucesso dentro da pasta', nome_pasta) # Imprimir uma mensagem indicando que o arquivo texto.txt foi criado com sucesso dentro da pasta
    except:
        pass

# Excluindo os arquivos txt e as pastas
for i in range(0, 10):
    nome_pasta = 'pasta' + str(i)
    try:
        os.remove(nome_pasta + '/texto.txt')
        print('Arquivo texto.txt excluído com sucesso dentro da pasta', nome_pasta) # Imprimir uma mensagem indicando que o arquivo texto.txt foi excluído com sucesso dentro da pasta
    except:
        pass
    
    try:
        os.rmdir(nome_pasta)
        print('Pasta', nome_pasta, 'excluída com sucesso.') # Imprimir uma mensagem indicando que a pasta foi excluída com sucesso
    except:
        print("Falha ao excluir pasta", nome_pasta)