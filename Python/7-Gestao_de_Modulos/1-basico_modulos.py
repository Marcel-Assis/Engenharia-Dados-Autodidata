import datetime as tempo #deu um alias
print(type(tempo)) # tipo módulo
data = tempo.datetime(1993,9,1,10,4,5) # ano, mês, dia, horas, minutos, segundos
print(data)

import random
print(random.randrange(10, 100)) # executa a função (randrange) que está dentro do módulo random

from random import randrange # importou a função direto no módulo
print(randrange(10,100)) # assim pode usar a função diretamente

from random import randrange as num_aleatorio # imprtou a função direto + alias
print(num_aleatorio(10, 100)) # usando a função como alias

from random import ranrange, randint # importa mais de uma função de um módulo

from random import * # importa todas as funções do módulo random