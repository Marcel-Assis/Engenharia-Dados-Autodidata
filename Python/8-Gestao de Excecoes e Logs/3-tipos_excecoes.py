# Diferentes Tipos de Exceções

### mais de um except
print("Início")
lista = [1, 2, 3]
try:
    print(lista[10])
except IndexError as erro1: # tratou um erro específico
    print("Falha ao acessar, index não encontrado", erro1)
except:
    print("Ocorreu outro erro") # caso ocorra qualquer outro erro diferente do indexerror
else:
    print("Executa se não ocorre erro")
print("Fim")