# Iteração em Arrays

import numpy as np
print('Percorrer array')
array = np.array([1,2,3,4])
print(array)
for i in array:
    print(i)

print('Percorrer matriz')
array2 = np.array([[1,2,3,4],[5,6,7,8]])
print(array2)
for i in array2:
    for j in i:
        print(j)


print('\nPercorrer matriz por coluna, usando nditer')
print(array2)
for x in np.nditer(array2, order='F'): # F = iteração coluna por coluna
    print(x)