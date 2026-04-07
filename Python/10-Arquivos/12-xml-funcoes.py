import xml.etree.ElementTree as xml # Importa a biblioteca para manipulação de XML
import os # Importa a biblioteca para manipulação de arquivos e diretórios

def criaTagPessoa(nome, cpf, sexo, endereco):
    no_pessoa = xml.Element("Pessoa", attrib={"nome": nome}) # Cria um nó filho "Pessoa" com um atributo "nome" e o valor do parâmetro "nome"
    no_cpf = xml.SubElement(no_pessoa, "CPF") # Cria um subnó "CPF" dentro do nó "Pessoa"
    no_cpf.text = cpf # Define o texto do nó "CPF" com o valor do parâmetro "cpf"
    no_sexo = xml.SubElement(no_pessoa, "Sexo") # Cria um subnó "Sexo" dentro do nó "Pessoa"
    no_sexo.text = sexo # Define o texto do nó "Sexo" com o valor do parâmetro "sexo"
    no_endereco = xml.SubElement(no_pessoa, "Endereço") # Cria um subnó "Endereço" dentro do nó "Pessoa"
    no_endereco.text = endereco # Define o texto do nó "Endereço" com o valor do parâmetro "endereco"
    return no_pessoa # Retorna o nó "Pessoa" criado

raiz = xml.Element("DadosPessoais") # Cria o nó raiz do XML com o nome "DadosPessoais"
pessoa1 = criaTagPessoa("Rodrigo", "123.456.789-00", "Masculino", "Rua A, 123") # Cria um nó "Pessoa" usando a função "criaTagPessoa" com os valores fornecidos

pessoa2 = criaTagPessoa("Maria", "987.654.321-00", "Feminino", "Rua B, 456") # Cria outro nó "Pessoa" usando a função "criaTagPessoa" com os valores fornecidos

pessoa3 = criaTagPessoa("João", "111.222.333-44", "Masculino", "Rua C, 789") # Cria mais um nó "Pessoa" usando a função "criaTagPessoa" com os valores fornecidos

raiz.append(pessoa1) # Adiciona o nó "Pessoa" criado como filho do nó raiz "DadosPessoais"
raiz.append(pessoa2) # Adiciona o segundo nó "Pessoa" criado como filho do nó raiz "DadosPessoais"
raiz.append(pessoa3) # Adiciona o terceiro nó "Pessoa" criado como filho do nó raiz "DadosPessoais"

arvore = xml.ElementTree(raiz) # Cria uma árvore XML a partir do nó raiz "DadosPessoais"
with open("dados_exemplo.xml", "wb") as files: # Abre um arquivo chamado "dados_exemplo.xml" em modo de escrita binária
    arvore.write(files) # Escreve a árvore XML no arquivo "dados_exemplo.xml" e fecha o arquivo automaticamente após a escrita