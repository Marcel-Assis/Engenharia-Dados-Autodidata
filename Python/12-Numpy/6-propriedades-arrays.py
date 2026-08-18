# Propriedades de Arrays

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,0])
print(array)
print(array.ndim) # mostra quantas dimensões tem o array
print(array.size) # numero de elementos totais
print(len(array)) # também mostra o número de elementos totais
print(array.shape) # mostra o formato (mais interessante quando tem mais de uma dimensão)
print(array.dtype) # mostra o tipo
print(array.itemsize) # mostra o tamanho do item
print(array.nbytes) # os bytes gastos pelo array total


# array de duas dimensões/matriz bidimensional
print('\n')
array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2)
print(array2.ndim) # mostra quantas dimensões tem o array
print(array2.size) # numero de elementos totais
print(len(array2)) # também mostra o número de elementos totais
print(array2.shape) # mostra o formato (mais interessante quando tem mais de uma dimensão)
print(array2.dtype) # mostra o tipo
print(array2.itemsize) # mostra o tamanho do item
print(array2.nbytes) # os bytes gastos pelo array total

# 
print('\n')
tipo_pessoa = np.dtype([('nome', 'S10'),('idade', 'i4')])
array3 = np.array([('Rodrigo', 24), ('Fernando', 45)], dtype= tipo_pessoa)
print(array3)
print(array3.ndim) # mostra quantas dimensões tem o array
print(array3.size) # numero de elementos totais
print(array3.shape) # mostra o formato (mais interessante quando tem mais de uma dimensão)
print(array3.dtype) # mostra o tipo
print(array3.itemsize) # mostra o tamanho do item
print(array3.nbytes) # os bytes gastos pelo array total