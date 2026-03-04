# Classes como atributos em Python
class Tipo1:
    def __init__(self, outra_classe): # Método construtor que recebe outra classe como atributo
        self.outra = outra_classe # Atributo que armazena a outra classe

class Tipo2:
    numero = 10 # Atributo de classe

classe2 = Tipo2() # Cria um objeto da classe Tipo2
classe1 = Tipo1(classe2) # Cria um objeto da classe Tipo1, passando o objeto classe2 como atributo

print(classe1.outra.numero) # Acessa o atributo de classe numero da classe Tipo2 através do objeto classe1