# Tratando Exceções

lista = [1,2,3]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador)) # haverá erro

while(True):
    try:
        print(next(iterador))
    except:
        break # se houver erro, encerra o laço