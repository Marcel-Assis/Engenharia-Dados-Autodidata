import xml.etree.ElementTree as xml # Importa a biblioteca para manipulação de XML
import os # Importa a biblioteca para manipulação de arquivos e diretórios

no_raiz = xml.Element("DadosPessoais") # Cria o nó raiz do XML com o nome "DadosPessoais"
no_pessoa = xml.Element("Pessoa", attrib={"nome": "Rodrigo"}) # Cria um nó filho "Pessoa" com um atributo "nome" e o valor "Rodrigo"
no_cpf = xml.SubElement(no_pessoa, "CPF") # Cria um subnó "CPF" dentro do nó "Pessoa"
no_cpf.text = "123.456.789-00" # Define o texto do nó "CPF" com o valor "123.456.789-00"
no_sexo = xml.SubElement(no_pessoa, "Sexo") # Cria um subnó "Sexo" dentro do nó "Pessoa"
no_sexo.text = "Masculino" # Define o texto do nó "Sexo" com o valor "Masculino"
no_endereco = xml.SubElement(no_pessoa, "Endereço") # Cria um subnó "Endereço" dentro do nó "Pessoa"
no_endereco.text = "Rua A, 123" # Define o texto do nó "Endereço" com o valor "Rua A, 123"

no_raiz.append(no_pessoa) # Adiciona o nó "Pessoa" como filho do nó raiz "DadosPessoais"

arvore = xml.ElementTree(no_raiz) # Cria uma árvore XML a partir do nó raiz "DadosPessoais"
with open("dados_exemplo.xml", "wb") as files: # Abre um arquivo chamado "dados_exemplo.xml" em modo de escrita binária
    arvore.write(files) # Escreve a árvore XML no arquivo "dados_exemplo.xml" e fecha o arquivo automaticamente após a escrita