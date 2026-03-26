# JSON (JavaScript Object Notation) é um formato leve de troca de dados, fácil de ler e escrever para humanos e fácil de analisar e gerar para máquinas. Ele é amplamente utilizado para transmitir dados entre um servidor e um cliente em aplicações web, mas também pode ser usado para armazenar dados em arquivos ou para comunicação entre diferentes sistemas. O JSON é baseado em uma estrutura de chave-valor, onde os dados são organizados em objetos (representados por chaves {}) e arrays (representados por colchetes []). Ele suporta tipos de dados como strings, números, booleanos, null, objetos e arrays. O módulo json do Python fornece funções para trabalhar com JSON, permitindo que você converta objetos Python em strings JSON e vice-versa. Para criar um arquivo JSON usando o módulo json, você pode seguir os seguintes passos:
import json
dados = {
    "pessoas": [
        {"id": 1, "nome": "João", "profissão": "Engenheiro"},
        {"id": 2, "nome": "Maria", "profissão": "Médica"},
        {"id": 3, "nome": "Pedro", "profissão": "Professor"}
    ]
}
with open("pessoas.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False) # Usar a função json.dump() para escrever os dados no arquivo JSON. O primeiro argumento é o objeto Python que você deseja converter em JSON (neste caso, o dicionário dados), o segundo argumento é o arquivo onde os dados serão escritos (neste caso, o arquivo "pessoas.json"). O parâmetro indent=4 é usado para formatar a saída JSON com uma indentação de 4 espaços, tornando-a mais legível. O parâmetro ensure_ascii=False é usado para garantir que os caracteres acentuados sejam exibidos corretamente na string JSON resultante. Sem esse parâmetro, os caracteres acentuados seriam escapados usando sequências de escape Unicode, o que pode tornar a string JSON menos legível. Com ensure_ascii=False, os caracteres acentuados serão mantidos como estão na string JSON, tornando-a mais legível e fácil de entender.
    print("Arquivo JSON criado com sucesso.") # Imprimir uma mensagem indicando que o arquivo JSON foi criado com sucesso
with open("pessoas.json", "r") as arquivo:
    dados_lidos = json.load(arquivo) # Usar a função json.load() para ler os dados do arquivo JSON. O argumento é o arquivo de onde os dados serão lidos (neste caso, o arquivo "pessoas.json"). A função json.load() converte o conteúdo do arquivo JSON em um objeto Python correspondente (neste caso, um dicionário).
    print(dados_lidos) # Imprimir os dados lidos do arquivo JSON. O resultado será um dicionário Python que representa a estrutura dos dados contidos no arquivo JSON.
    for pessoa in dados_lidos["pessoas"]: # Usar um loop for para iterar sobre a lista de pessoas contida no dicionário lido do arquivo JSON. A chave "pessoas" é usada para acessar a lista de pessoas dentro do dicionário.
        print(f"ID: {pessoa['id']}, Nome: {pessoa['nome']}, Profissão: {pessoa['profissão']}") # Imprimir as informações de cada pessoa. A sintaxe pessoa['id'], pessoa['nome'] e pessoa['profissão'] é usada para acessar os valores correspondentes às chaves "id", "nome" e "profissão" de cada dicionário que representa uma pessoa na lista.
