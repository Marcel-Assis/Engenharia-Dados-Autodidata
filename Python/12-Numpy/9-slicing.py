# Slicing

import numpy  as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print(array[2]) # acessando a terceira linha (index 2 do array)
print(array[2][2]) # acessa na terceira linha, o terceiro elemento
print(array[2,2]) # mesmo resultado de cima, mas outra sintaxe
print(array[1:3]) # vai acessar as listas da posição 1 ao 2 
print(array[2,1:3]) # vai acessar do índice 2 (terceira linha) a posição 1 ao 2

# : serve pra acessar a linha ou a coluna inteira, depende da ordem que colocar, esquerda linha, direita coluna
print(array[2, :]) # vai acessar a linha 2 inteira
print(array[:, 2]) # vai acessar a terceira coluna inteira (3, 6, 9)

array2 = np.array([[1,2,3,4],[5,6,7,8]]) # cria uma matriz 2x4
print(array2)
print(array2[1, :]) # acessa a linha 1 inteira
print(array2[:, 2]) # acessa a coluna 2 inteira

array3 = np.array([[1,2,3,4,5,6,7,8,9],
                  [10,11,12,13,14,15,16,17,18],
                  [19,20,21,22,23,24,25,26,27]])
print(array3)
print(array3[1, 1:5]) # toda a linha do índice 1, os índices de 1 ao 4
print(array3[1, 0:8:2]) # toda a linha 1, da posição 0 à 8, de 2 em 2
print(array3[1, ::2]) # toda a linha 1, de 2 em 2