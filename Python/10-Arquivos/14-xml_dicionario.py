# Criando XML a partir de um Dicionário

import xml.etree.ElementTree as xml
import os

def criaTagPessoa(nome, cpf, sexo, endereco): # passa os parâmetros dos nós
    no_pessoa = xml.Element("Pessoa", attrib={'Nome': nome}) # define um atributo pro elemento criado

    # Criando as sub tags
    no_cpf = xml.SubElement(no_pessoa, 'CPF') # cria uma tag filha de pessoa (subelemento de pessoa)
    no_cpf.text = cpf # define o valor do subelemento

    no_sexo = xml.SubElement(no_pessoa, 'Sexo') # cria uma tag filha de pessoa (subelemento de pessoa)
    no_sexo.text = sexo # define o valor do subelemento

    no_endereco = xml.SubElement(no_pessoa, 'Endereco') # cria uma tag filha de pessoa (subelemento de pessoa)
    no_endereco.text = endereco # define o valor do subelemento

    return no_pessoa # retorna o nó pessoa

# dicionário
dados = {
    'Rodrigo': {
        "cpf": "12345",
        "sexo": "masculino",
        'Endereco': 'rua x',
        'idade': 32
    },
    'Fernanda': {
        "cpf": "54321",
        "sexo": "feminino",
        'Endereco': 'rua y',
        'idade': 23,
        'filhos': ['Rodrigo', 'Lucas']
    },
        'Ana': {
        "cpf": "654321",
        "sexo": "feminino",
        'Endereco': 'rua z',
        'idade': 31
    },
}


raiz = xml.Element("DadosPessoais")

# percorrer o dicionário
for key in dados: # pra cada elemento do dicionário (rodrigo, fernanda)
    nome = key # passa o elemento pra variável nome
    dados_pessoa = dados[nome] # passa o elemento (dados['Rodrigo']) pra variável dados_pessoa
    cpf = dados_pessoa['cpf'] # nome da chave (cpf) do dicionário
    sexo = dados_pessoa['sexo'] # nome da chave (sexo) do dicionário
    endereco = dados_pessoa['Endereco'] # nome da chave (endereco) do dicionário
    # idade = dados_pessoa['Idade'] # nome da chave (idade) do dicionário
    pessoa = criaTagPessoa(nome, cpf, sexo, endereco) # sem idade pois a função não possui a tag idade
    if 'filhos' in dados_pessoa:
        filhos = xml.SubElement(pessoa, 'filhos')
        for filho in dados_pessoa['filhos']: # pra cada elemento filhos em dados_pessoa
            pessoa_filho = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})
    raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais_3.xml', 'wb') as file:
    arvore.write(file)