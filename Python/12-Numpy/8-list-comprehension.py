# List Comprehension

import numpy as np

array = np.array([i for i in range(0,10)]) # cria uma lista de 0 a 9
print(array)

array2 = np.array([[i for i in range(0, 3)],
                  [i for i in range(3, 6)],
                  [i for i in range(6, 9)]]
                  ) # cria uma matriz bidimensional 3x3
print(array2)