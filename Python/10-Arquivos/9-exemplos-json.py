import json

idades = {
    "João": 30,
    "Maria": 25,
    "Pedro": 35
}

json.dumps(idades) # A função json.dumps() é usada para converter um objeto Python em uma string JSON. Neste caso, a variável idades, que é um dicionário Python, será convertida em uma string JSON que representa a mesma estrutura de dados.

print(json.dumps(idades, ensure_ascii=False)) # O parâmetro ensure_ascii=False é usado para garantir que os caracteres acentuados sejam exibidos corretamente na string JSON resultante. Sem esse parâmetro, os caracteres acentuados seriam escapados usando sequências de escape Unicode, o que pode tornar a string JSON menos legível. Com ensure_ascii=False, os caracteres acentuados serão mantidos como estão na string JSON, tornando-a mais legível e fácil de entender.
print(json.dumps(30)) # A função json.dumps() pode ser usada para converter diferentes tipos de objetos Python em strings JSON. Neste caso, o número inteiro 30 será convertido em uma string JSON que representa o valor numérico 30.
print(json.dumps("Olá, mundo!", ensure_ascii=False)) # A função json.dumps() pode ser usada para converter diferentes tipos de objetos Python em strings JSON. Neste caso, a string "Olá, mundo!" será convertida em uma string JSON que representa o mesmo texto. O resultado será uma string JSON que inclui as aspas duplas ao redor do texto, indicando que é uma string JSON válida.
print(json.dumps([1, 2, 3, 4, 5])) # A função json.dumps() pode ser usada para converter diferentes tipos de objetos Python em strings JSON. Neste caso, a lista [1, 2, 3, 4, 5] será convertida em uma string JSON que representa a mesma estrutura de dados. O resultado será uma string JSON que inclui os colchetes ao redor dos números, indicando que é um array JSON válido.
print(json.dumps({"nome": "João", "idade": 30}, ensure_ascii=False)) # A função json.dumps() pode ser usada para converter diferentes tipos de objetos Python em strings JSON. Neste caso, o dicionário {"nome": "João", "idade": 30} será convertido em uma string JSON que representa a mesma estrutura de dados. O resultado será uma string JSON que inclui as chaves ao redor dos pares de chave-valor, indicando que é um objeto JSON válido. A string JSON resultante será: {"nome": "João", "idade": 30}.


###

DadosPessoas = {
    'Rodrigo': {
        'CPF': '123.456.789-00',
        'Sexo': 'Masculino',
        'Endereço': 'Rua A, 123',
        'Idade': 30
    },
    'Maria': {
        'CPF': '987.654.321-00',
        'Sexo': 'Feminino',
        'Endereço': 'Rua B, 456',
        'Idade': 25,
        'Filhos': ['João', 'Ana']
    }
}
texto = json.dumps(DadosPessoas, indent=4, ensure_ascii=False) # A função json.dumps() é usada para converter um objeto Python em uma string JSON. Neste caso, a variável DadosPessoas, que é um dicionário Python, será convertida em uma string JSON que representa a mesma estrutura de dados. O parâmetro indent=4 é usado para formatar a saída JSON com uma indentação de 4 espaços, tornando-a mais legível. O parâmetro ensure_ascii=False é usado para garantir que os caracteres acentuados sejam exibidos corretamente na string JSON resultante. Sem esse parâmetro, os caracteres acentuados seriam escapados usando sequências de escape Unicode, o que pode tornar a string JSON menos legível. Com ensure_ascii=False, os caracteres acentuados serão mantidos como estão na string JSON, tornando-a mais legível e fácil de entender.
print(texto) # Imprimir a string JSON resultante. O resultado será uma representação em formato JSON do dicionário DadosPessoas, com uma indentação de 4 espaços para facilitar a leitura e os caracteres acentuados exibidos corretamente.

with open('exemplo.json', 'wt', encoding='utf-8') as arquivo:
    arquivo.write(texto)
###

dicionario = None
with open('exemplo.json', 'rt', encoding='utf-8') as arquivo:
    arquivo_lido = arquivo.read() # A função json.read() é usada para ler o conteúdo de um arquivo JSON e convertê-lo em um objeto Python correspondente. Neste caso, o arquivo 'exemplo.json' é aberto em modo de leitura ('rt') com codificação UTF-8, e a função json.read() é chamada para ler o conteúdo do arquivo e armazená-lo na variável dicionario. O resultado será um objeto Python (neste caso, um dicionário) que representa a estrutura dos dados contidos no arquivo JSON.
    dicionario = json.loads(arquivo_lido) # A função json.loads() é usada para ler o conteúdo de uma string JSON e convertê-la em um objeto Python correspondente. Neste caso, a variável arquivo_lido, que contém o conteúdo do arquivo JSON lido anteriormente, é passada como argumento para a função json.loads(). O resultado será um objeto Python (neste caso, um dicionário) que representa a estrutura dos dados contidos no arquivo JSON.
print(dicionario) # Imprimir o objeto Python resultante da leitura do arquivo JSON. O resultado será um dicionário Python que representa a estrutura dos dados contidos no arquivo JSON.