# Override (Sobrescrição) de métodos em Python
class Animal: # Classe base (superclasse)
    def __init__(self, nome): # Método construtor da classe
        self.nome = nome # Atributo de instância
    
    def fazer_som(self): # Método da classe
        pass # Método que será sobrescrito pelas subclasses

class Cachorro(Animal): # Subclasse que herda da classe Animal
    def fazer_som(self): # Sobrescreve o método da classe base
        return "Au au" # Implementação específica para a subclasse

class Gato(Animal): # Subclasse que herda da classe Animal
    def fazer_som(self): # Sobrescreve o método da classe base
        return "Miau" # Implementação específica para a subclasse

cachorro = Cachorro("Rex")
gato = Gato("Mimi")

print(cachorro.fazer_som()) # Saída: Au au
print(gato.fazer_som()) # Saída: Miau