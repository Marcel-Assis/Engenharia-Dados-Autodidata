# Outras Formas de Declarar Tipos

import numpy

# array numeros
array = numpy.array([1,2,3,4,5,6,7,8,9,0])
print(array, type(array))
print(array.dtype)

# definir o tipo
array2 = numpy.array([1,2,3,4,5,6,7,8,9,0], dtype= numpy.int8)
print(array2, type(array2))
print(array2.dtype)

# array texto
array3 = numpy.array(['1', '234', '1'], dtype= numpy.str_)
print(array3, type(array3))
print(array3.dtype) # mostra quantos bites está utilizando (no caso 3 pois há um texto com 3 caracteres)

# padrões para definir o tipo
# i = inteiro
# b = booleano
# u = inteiro sem sinal
# f = ponto flutuante
# S = String (bytes)
# U = String Unicode

array4 = numpy.array(['abc', 'def', 'ghi'], dtype= 'S3') # define o tipo e o tamanho (String e 3 bytes)
print(array4, type(array4))
print(array4.dtype) # tipo
print(array4.itemsize) # tamanho (bits) de cada item
print(array4.nbytes) # total de bits do array

array5 = numpy.array([1,2,3], dtype= 'i2') # define o tipo e o tamanho (inteiro e 2 bytes)
print(array5, type(array5))
print(array5.dtype) # tipo
print(array5.itemsize) # tamanho (bits) de cada item
print(array5.nbytes) # total de bits do array

