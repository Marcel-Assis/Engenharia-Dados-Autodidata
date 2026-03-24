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

# O código acima tenta deletar a pasta "nova_pasta" usando a função os.rmdir(). Se a pasta não existir, ele captura a exceção FileNotFoundError e imprime uma mensagem indicando que a pasta não existe. Independentemente de a pasta ter sido deletada ou não, o bloco finally é executado, criando a pasta "nova_pasta" novamente usando a função os.mkdir() e imprimindo uma mensagem indicando que a pasta foi criada com sucesso.
