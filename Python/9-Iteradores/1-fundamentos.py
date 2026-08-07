# Fundamentos

# Iteradores são objetos que podem ser percorridos, que são iteráveis

# Exemplo

lista = [1,2,3,4]
iterador = iter(lista) # iter é um método do python para iterar, usei pra iterar a lista
print(next(iterador)) # o next posiciona no primeiro elemento, depois no segundo, etc
print(next(iterador))
print(next(iterador))
print(next(iterador))

for item in lista:
    print(item)

print(1 in lista) # retorna True