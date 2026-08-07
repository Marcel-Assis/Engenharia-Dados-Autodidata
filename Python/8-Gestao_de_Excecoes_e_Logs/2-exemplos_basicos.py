# Exemplos Básicos

# print("Início")
# lista = [1, 2, 3]
# print(lista[10]) # Erro de index fora de área
# print("Fim")

### try e except
print("Início")
lista = [1, 2, 3]
try:
    print(lista[10])
except:
    print("Falha ao acessar, index não encontrado")
print("Fim")

### except com alias + mensagem de erro
print("Início")
lista = [1, 2, 3]
try:
    print(lista[10])
except Exception as erro: # Passa o erro pra um alias
    print("Falha ao acessar, index não encontrado, mensagem:", str(erro)) # Mostra qual o erro sem quebrar o programa
print("Fim")

###  finally
print("Início")
lista = [1, 2, 3]
try:
    print(lista[10])
except:
    print("Falha ao acessar, index não encontrado")
finally: # executa sempre que o try-except acabar, mesmo sem erro
    del lista 
print("Fim")

### else
print("Início")
lista = [1, 2, 3]
try:
    print(lista[1]) # pula pro else
except:
    print("Falha ao acessar, index não encontrado")
else: # executa somente se não houver erro
    print("Não houve erro")
print("Fim")

### finally adicionado com else
print("Início")
lista = [1, 2, 3]
try: # código que pode dar erro
    print(lista[1]) # pula pro else
except: # código executado se der erro
    print("Falha ao acessar, index não encontrado")
else: # código executado se não der erro
    print("Não houve erro")
finally: # código executado sempre
    print("Executa sempre")
print("Fim")