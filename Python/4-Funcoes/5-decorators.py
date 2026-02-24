# Decorators:
# Explicação -> Um decorator é uma função que recebe outra função como argumento e retorna uma nova função com comportamento adicional.
# Eles são úteis para adicionar funcionalidades a funções existentes sem modificar seu código.

def meu_decorator(func):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        func()
        print("Algo está acontecendo depois da função ser chamada.")
    return wrapper

@meu_decorator
def diz_ola():
    print("Olá!")

diz_ola()

# Outro exemplo:
def outro_decorator(func):
    def wrapper():
        print("Antes da execução da função.")
        func()
        print("Depois da execução da função.")
    return wrapper

@outro_decorator
def diz_adeus():
    print("Adeus!")

diz_adeus()