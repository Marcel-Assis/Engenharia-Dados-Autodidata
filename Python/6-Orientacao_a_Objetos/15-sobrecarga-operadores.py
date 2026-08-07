# Sobrecarga de operadores em Python

class Ponto:
    def __init__(self, x, y): # Método construtor
        self.x = x
        self.y = y

    def __add__(self, outro): # Sobrecarga do operador +
        return Ponto(self.x + outro.x, self.y + outro.y) # Retorna um novo objeto Ponto

    def __sub__(self, outro): # Sobrecarga do operador -
        return Ponto(self.x - outro.x, self.y - outro.y) # Retorna um novo objeto Ponto

    def __str__(self): # Sobrecarga do método str
        return f'({self.x}, {self.y})' # Retorna a representação em string do objeto

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

print(p1 + p2)  # Saída: (4, 6)
print(p1 - p2)  # Saída: (-2, -2)
