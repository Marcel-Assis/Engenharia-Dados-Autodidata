# Propriedades de objetos em Python
class Pessoa: # Classe que representa uma pessoa
    def __init__(self, nome, idade): # Método construtor da classe
        self._nome = nome # Atributo privado que armazena o nome da pessoa
        self._idade = idade # Atributo privado que armazena a idade da pessoa
        print(f"Objeto criado: {self._nome}, {self._idade} anos") # Mensagem exibida quando o objeto é criado

pessoa1 = Pessoa("Alice", 30) # Cria um objeto da classe Pessoa
pessoa2 = Pessoa("Bob", 25) # Cria outro objeto da classe Pessoa

print(pessoa1._nome) # Acessa o atributo privado _nome do objeto pessoa1
print(pessoa2._idade) # Acessa o atributo privado _idade do objeto pessoa2