import random

print(f'random: {dir(random)}') # trás listas, funções, atributos e classes de dentro do módulo
print(f'\nrandrange: {dir(random.randrange)}') # trás detalhes especificamente dessa função
print(f'\nname: {random.__name__}') # o nome
print(f'\nfile: {random.__file__}') # a onde está o arquivo das funções
print(f'\ndoc: {random.__doc__}') # a documentação
