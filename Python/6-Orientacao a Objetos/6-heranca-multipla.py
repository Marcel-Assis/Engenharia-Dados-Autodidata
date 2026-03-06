# Herança múltipla em Python
class Base1:
    def __init__(self, atributo1):
        self.atributo1 = atributo1
        print("Construtor da Base1 e atributo1:", self.atributo1)

class Base2:
    def __init__(self, atributo2):
        self.atributo2 = atributo2
        print("Construtor da Base2 e atributo2:", self.atributo2)

class Derivada(Base1, Base2): # Subclasse que herda de Base1 e Base2
    def __init__(self, atributo1, atributo2):
        Base1.__init__(self, atributo1)  # Chama o construtor da primeira classe base
        Base2.__init__(self, atributo2)  # Chama o construtor da segunda classe base

obj = Derivada(10, 20)  # Cria uma instância da classe Derivada e chama os construtores das classes base