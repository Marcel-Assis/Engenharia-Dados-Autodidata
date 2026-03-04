# Herança em Python
class Veiculo: # Classe base (superclasse)
    def __init__(self, marca, modelo): # Método construtor da classe
        self.marca = marca # Atributo de instância
        self.modelo = modelo # Atributo de instância

class Carro(Veiculo): # Subclasse que herda da classe Veiculo
    def __init__(self, marca, modelo, portas): # Método construtor da subclasse
        super().__init__(marca, modelo) # Chama o construtor da classe base
        self.portas = portas # Atributo específico da subclasse

class Moto(Veiculo): # Subclasse que herda da classe Veiculo
    def __init__(self, marca, modelo, cilindradas): # Método construtor da subclasse
        super().__init__(marca, modelo) # Chama o construtor da classe base
        self.cilindradas = cilindradas # Atributo específico da subclasse
    
carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR500R", 500)

print(carro.marca, carro.modelo, carro.portas) # Saída: Toyota Corolla 4
print(moto.marca, moto.modelo, moto.cilindradas) # Saída: Honda CBR500R 500