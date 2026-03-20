from os import path

arquivo_existe = path.exists("exemplo.txt") # Verificar se o arquivo "exemplo.txt" existe usando a função path.exists() do módulo os.path. Esta função retorna True se o arquivo existir e False caso contrário.

if arquivo_existe: # Verificar se o arquivo existe
    print("O arquivo existe.") # Imprimir uma mensagem indicando que o arquivo existe
else:
    print("O arquivo não existe.") # Imprimir uma mensagem indicando que o arquivo não existe