# Métodos estáticos
# Métodos que pertencem à classe, mas não dependem da instância
class Teste:
    def __init__(self):
        pass
    @classmethod # método de classe
    def class_method(cls): # recebe a instancia da classe como primeiro argumento
        print(f'Este é um método de classe da classe {cls.__name__}')
    @staticmethod # método estático
    def static_method(): # não recebe nem a instância nem a classe como argumento
        print("Este é um método estático")

Teste.class_method() # chamando método de classe
Teste.static_method() # chamando método estático