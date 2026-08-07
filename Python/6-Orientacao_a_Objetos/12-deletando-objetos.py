# Deletando objetos em Python

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa("Alice")
p2 = Pessoa("Bob")

print(p1.nome)
print(p2.nome)

del p1
del p2