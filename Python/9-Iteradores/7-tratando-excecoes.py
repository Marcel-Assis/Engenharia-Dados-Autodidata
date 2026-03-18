
lista = [1,2,3]
iterador = iter(lista)
print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
# print(next(iterador))  # Isso gerará um erro StopIteration, pois não há mais elementos para iterar.

# Para evitar o erro StopIteration, podemos usar um bloco try-except para capturar a exceção e encerrar o loop quando não houver mais elementos para iterar. Isso é especialmente útil quando estamos iterando sobre um iterador em um loop while, onde não sabemos quantos elementos existem.
while(True):
    try:
        print(next(iterador))  # Tente obter o próximo elemento do iterador
    except: 
        break  # Encerre o loop para evitar um loop infinito