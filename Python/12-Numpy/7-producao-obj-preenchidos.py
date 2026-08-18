# Produção de Objetos Preenchidos

import numpy as np

array1 = np.zeros(9) # cria uma array de 0, 9 vezes
array2 = np.ones(3) # cria um array de 1, 3 vezes
array3 = np.empty(6) # cria um array "vazio", 6 vezes
array4 = np.identity(4) # cria um array (nesse caso 4x4) com o número 1 preenchendo toda a diagonal, de cima pra baixo, da esquerda pra direita
print(array1)
print(array2)
print(array3)
print(array4)

array5 = np.zeros((3,3)) # cria uma matriz de 0, com 3 linhas e 3 colunas
array6 = np.ones((4,4)) # cria um array de 1, 4x4
print(array5)
print(array6)

array7 = np.arange(9) # cria um array de 0 a 8
print(array7)
array8 = np.arange(4,16) # cria um array de 4 a 15
print(array8)

array9 = np.arange(2,16+1,2) # cria um array de 2 a 16, de 2 em 2
print(array9)

array10 = np.full((4,4), 10) # cria uma matriz 4x4 preenchida com 10
print(array10)

array11_float = np.random.rand(4,4) # cria um array de 4x4 com floats aleatórios
print(array11_float)

array12_int = np.random.randint(5,11, (5,5)) # cria uma matriz do 5 ao 10 de tamanho 5x5
print(array12_int)