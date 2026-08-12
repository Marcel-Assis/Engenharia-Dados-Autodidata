# Criando um XML


import xml.etree.ElementTree as xml
import os

no_raiz = xml.Element("DadosPessoais") # cria um nó
no_pessoa = xml.Element("Pessoa", attrib={'Nome': 'Rodrigo'}) # define um atributo pro elemento criado

no_cpf = xml.SubElement(no_pessoa, 'CPF') # cria uma tag filha de pessoa (subelemento de pessoa)
no_cpf.text = '123456' # define o valor do subelemento

no_sexo = xml.SubElement(no_pessoa, 'Sexo') # cria uma tag filha de pessoa (subelemento de pessoa)
no_sexo.text = 'Masculino' # define o valor do subelemento

no_endereco = xml.SubElement(no_pessoa, 'Endereco') # cria uma tag filha de pessoa (subelemento de pessoa)
no_endereco.text = 'Rua x' # define o valor do subelemento

no_raiz.append(no_pessoa) # passa o nó pessoa pro nó raiz

arvore = xml.ElementTree(no_raiz) # transforma o nó raiz em xml

with open('dados_exemplo.xml', 'wb') as files:
    arvore.write(files)