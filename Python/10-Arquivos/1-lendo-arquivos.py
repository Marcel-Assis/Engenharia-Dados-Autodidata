# Lendo arquivos em Python
# Para ler um arquivo em Python, você pode usar a função `open()`, que retorna um objeto de arquivo. Você pode usar o método `read()` para ler o conteúdo do arquivo como uma string, ou o método `readlines()` para ler o conteúdo do arquivo como uma lista de linhas. Aqui está um exemplo de como ler um arquivo em Python:
# Abrir o arquivo para leitura
arquivo = open('exemplo.txt', 'r')
# Ler o conteúdo do arquivo
conteudo = arquivo.read()
# Imprimir o conteúdo do arquivo
print(conteudo)
# Fechar o arquivo
arquivo.close()
# É importante lembrar de fechar o arquivo após a leitura para liberar os recursos do sistema. Você também pode usar a declaração `with` para garantir que o arquivo seja fechado automaticamente, mesmo que ocorra um erro durante a leitura. Aqui está um exemplo usando a declaração `with`:
# Usar a declaração with para abrir o arquivo
with open('exemplo.txt', 'r') as arquivo:
    # Ler o conteúdo do arquivo
    conteudo = arquivo.read()
    # Imprimir o conteúdo do arquivo
    print(conteudo)
# Neste exemplo, o arquivo será fechado automaticamente após a execução do bloco `with`, mesmo que ocorra um erro durante a leitura.
# Se você quiser ler o arquivo linha por linha, pode usar um loop `for` para iterar sobre o objeto de arquivo. Aqui está um exemplo:
# Usar a declaração with para abrir o arquivo
with open('exemplo.txt', 'r') as arquivo:
    # Iterar sobre cada linha do arquivo
    for linha in arquivo:
        # Imprimir a linha
        print(linha.strip())  # Usar strip() para remover espaços em branco extras
# Neste exemplo, o loop `for` itera sobre cada linha do arquivo e imprime a linha, removendo quaisquer espaços em branco extras usando o método `strip()`.
# Você também pode usar o método `readlines()` para ler todas as linhas do arquivo em uma lista. Aqui está um exemplo:
# Usar a declaração with para abrir o arquivo
with open('exemplo.txt', 'r') as arquivo:
    # Ler todas as linhas do arquivo em uma lista
    linhas = arquivo.readlines()
    # Imprimir a lista de linhas
    print(linhas)
# Neste exemplo, o método `readlines()` lê todas as linhas do arquivo e as armazena em uma lista chamada `linhas`, que é então impressa. Cada elemento da lista representa uma linha do arquivo, incluindo o caractere de nova linha (`\n`) no final de cada linha.
# Lembre-se de substituir `'exemplo.txt'` pelo caminho do arquivo que você deseja ler. Certifique-se de que o arquivo exista e esteja no mesmo diretório do seu script Python ou forneça o caminho completo para o arquivo.

# Parametros de abertura de arquivos:
# 'r' - Modo de leitura (padrão)
# 'w' - Modo de escrita (cria um novo arquivo ou sobrescreve um arquivo existente)
# 'a' - Modo de anexação (adiciona conteúdo a um arquivo existente)
# 'b' - Modo binário (usado para arquivos binários, como imagens ou arquivos de áudio)
# 't' - Modo de texto (padrão para arquivos de texto)
# 'x' - Modo de criação exclusiva (cria um novo arquivo, mas falha se o arquivo já existir)
# 'r+' - Modo de leitura e escrita (permite ler e escrever em um arquivo existente)
# 'w+' - Modo de escrita e leitura (cria um novo arquivo ou sobrescreve um arquivo existente, permitindo ler e escrever)
# 'a+' - Modo de anexação e leitura (adiciona conteúdo a um arquivo existente, permitindo ler e escrever)
# 'x+' - Modo de criação exclusiva e leitura (cria um novo arquivo, mas falha se o arquivo já existir, permitindo ler e escrever)
# 'rt' - Modo de leitura em texto (padrão para arquivos de texto)
# 'rb' - Modo de leitura em binário (usado para arquivos binários)
# 'wt' - Modo de escrita em texto (cria um novo arquivo ou sobrescreve um arquivo existente)
# 'wb' - Modo de escrita em binário (usado para arquivos binários)
# 'at' - Modo de anexação em texto (adiciona conteúdo a um arquivo existente)
# 'ab' - Modo de anexação em binário (usado para arquivos binários)
# 'xt' - Modo de criação exclusiva em texto (cria um novo arquivo, mas falha se o arquivo já existir)
# 'xb' - Modo de criação exclusiva em binário (usado para arquivos binários)