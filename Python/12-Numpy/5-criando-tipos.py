# Criando Nossos Tipos
import numpy

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

array = numpy.array([Pessoa('Fernando', 45), Pessoa('Rodrigo', 23)])
print(array)
print(type(array))
print(array.dtype, end='\n\n')
print(array[0].nome, array[1].idade)

# --

tipo_pessoa = numpy.dtype([('nome', 'S10'),('idade', 'i4')])
array2 = numpy.array([('Rodrigo', 24), ('Fernando', 45)], dtype= tipo_pessoa)
print(array2)
print(type(array2))
print(array2.dtype)