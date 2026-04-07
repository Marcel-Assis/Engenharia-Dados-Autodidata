import xml.etree.ElementTree as xml
import os

def criaTagPessoa(nome, cpf, sexo, endereco):
    no_pessoa = xml.Element("Pessoa", attrib={"nome": nome})
    no_cpf = xml.SubElement(no_pessoa, "CPF")
    no_cpf.text = cpf
    no_sexo = xml.SubElement(no_pessoa, "Sexo")
    no_sexo.text = sexo
    no_endereco = xml.SubElement(no_pessoa, "Endereço")
    no_endereco.text = endereco
    return no_pessoa

raiz = xml.Element("DadosPessoais")

dados = {
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
    },
        'Ana': {
        'CPF': '123.456.789-00',
        'Sexo': 'Feminino',
        'Endereço': 'Rua A, 123',
        'Idade': 28
    },
}

raiz = xml.Element("DadosPessoais")
for key in dados:
    nome = key
    dados_pessoa = dados[nome]
    cpf = dados_pessoa['CPF']
    sexo = dados_pessoa['Sexo']
    endereco = dados_pessoa['Endereço']
    # idade = dados_pessoa['Idade']
    pessoa = criaTagPessoa(nome, cpf, sexo, endereco)
    raiz.append(pessoa)
    if 'Filhos' in dados_pessoa:
        filhos = xml.SubElement(pessoa, "Filhos")
        for filho in dados_pessoa['Filhos']:
            pessoa_filho = xml.SubElement(filhos, "Pessoa", attrib={"nome": filho})
            
    raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais.xml', 'wb') as arquivo:
    arvore.write(arquivo)