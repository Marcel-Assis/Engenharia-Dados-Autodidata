# Herança múltipla em Python
class Base1:
    def __init__(self):
        print("Construtor da Base1")

class Base2:
    def __init__(self):
        print("Construtor da Base2")

class Derivada(Base1, Base2): # Subclasse que herda de Base1 e Base2
    def __init__(self):
        Base1.__init__(self)  # Chama o construtor da primeira classe base
        Base2.__init__(self)  # Chama o construtor da segunda classe base

obj = Derivada()  # Cria uma instância da classe Derivada e chama os construtores das classes base