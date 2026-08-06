# Gerando as Próprias Exceções

### raise - força uma exceção
def printa_positivo(numero):
    if numero < 0:
        raise ValueError("Valor não pode ser negativo") # gera uma exceção própria
    print(numero)

try:
    printa_positivo(-1)
except ValueError as erro1: # pega a exceção própria que foi gerada e trata
    print("O erro é", erro1)


### assert - teste lógico
def printa_positivo(numero):
    assert(numero >= 0) # se não passar no teste lógico, gera um assertion error
    print(numero)

try:
    printa_positivo(-1)
except AssertionError as erro1: # pega a exceção própria que foi gerada e trata
    print("O erro é", erro1)