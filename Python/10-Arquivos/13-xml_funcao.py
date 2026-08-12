# Utilizando XML com Funções

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

raiz = xml.Element("DadosPessoais") # Cria o elemento raiz

# Cria as pessoas
pessoa1 = criaTagPessoa('Rodrigo', '123456', 'Masculino', 'Rua x')
pessoa2 = criaTagPessoa('Maria', '654321', 'Feminino', 'Rua y')
pessoa3 = criaTagPessoa('Ana', '123654', 'Feminino', 'Rua z')

# Salva as pessoas no nó raiz
raiz.append(pessoa1)
raiz.append(pessoa2)
raiz.append(pessoa3)

arvore = xml.ElementTree(raiz) # cria a arvora

with open('dados_exemplo.xml', 'wb') as files:
    arvore.write(files)