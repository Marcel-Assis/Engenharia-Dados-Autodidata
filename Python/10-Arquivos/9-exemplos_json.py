# Exemplos com Json
import json

 # cria o objeto dicionário idades
idades = {
    'Rogério': 20,
    'Maria': 34,
    'Pedro': 18
}

# função dumps transforma objetos do python em json
print(json.dumps(idades)) # ensure_ascii=False interpreta o caractere acentuado
print(json.dumps(idades, ensure_ascii=False)) # ensure_ascii=False interpreta o caractere acentuado
print(json.dumps(23))
print(json.dumps(3.14))
print(json.dumps([1,2,3,4,5]))
print(json.dumps(True))
print(json.dumps(None))

 # cria o objeto dicionário DadosPessoais
DadosPessoais = {
    'Rodrigo': {
        "cpf": "12345",
        "sexo": "masculino",
        'Endereço': 'rua x',
        'idade': 32
    },
    'Fernanda': {
        "cpf": "54321",
        "sexo": "feminino",
        'Endereço': 'rua y',
        'idade': 23,
        'Filhos': ['Rodrigo', 'Lucas']
    }
}

texto = json.dumps(DadosPessoais, ensure_ascii=False, indent=4) # indent diz o nível de indentação que a gente quer (nesse caso, 4 espaços)
print(texto)

# cria o arquivo exemplo.json
with open('exemplo.json', 'wt') as arquivo:
    arquivo.write(texto)

# ler um arquivo json e transformar em dicionário
dicionario = None
with open('exemplo.json', 'rt') as arquivo: # arquivo aberto
    arquivo_lido = arquivo.read() # arquivo lido
    dicionario = json.loads(arquivo_lido) # loads passa o arquivo_lido pro objeto dicionario

print(dicionario)
print(f'Idade do Rodrigo: ', dicionario['Rodrigo']['idade']) # do Rodrigo, eu quero a idade