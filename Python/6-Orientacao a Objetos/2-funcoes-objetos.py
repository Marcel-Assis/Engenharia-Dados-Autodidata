# Funções de objetos em Python
class Pessoa: # Classe que representa uma pessoa
    def __init__(self, nome, idade): # Método construtor da classe
        self._nome = nome # Atributo privado que armazena o nome da pessoa
        self._idade = idade # Atributo privado que armazena a idade da pessoa
        print(f"Objeto criado: {self._nome}, {self._idade} anos") # Mensagem exibida quando o objeto é criado
    
    def aniversario(self): # Método que incrementa a idade da pessoa
        self._idade += 1 # Incrementa a idade em 1
        print(f"Feliz aniversário, {self._nome}! Agora você tem {self._idade} anos.") # Mensagem exibida quando a pessoa faz aniversário
    
pessoa1 = Pessoa("Alice", 30) # Cria um objeto da classe Pessoa
pessoa1.aniversario() # Chama o método aniversario do objeto pessoa1
print(pessoa1._idade) # Acessa o atributo privado _idade do objeto pessoa1