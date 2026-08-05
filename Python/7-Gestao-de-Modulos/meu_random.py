import random
def get_random_lista(inicial, final, tam):
    lista = []
    for i in range(0, tam):
        numero_aleatorio = random.randrange(inicial, final)
        lista.append(numero_aleatorio)
    return lista
