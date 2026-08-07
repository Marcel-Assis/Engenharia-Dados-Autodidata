# Funções Iteráveis - Generators

# yield é como se fosse uma âncora pro iterador, ele basicamente salva o estado desde a última vez que a função foi chamada
# Exemplo:

def ancora(): # Simplesmente uma função que é iterável (por conta do yield)
    yield 2
    yield 1
    yield 3

for item in ancora():
    print(item)

print(10 in ancora()) # False
print(2 in ancora()) # True


# Utilizando o next
func = ancora()
print(next(func))
print(next(func))
print(next(func))

# Criando uma função iterável
def meu_range(num):
    local_num = 0
    while local_num < num:
        yield local_num
        local_num += 1

for i in meu_range(6):
    print(i)