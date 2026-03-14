# A função enumerate é usada para iterar sobre uma sequência, como uma lista ou uma tupla, e obter tanto o índice quanto o valor do elemento ao mesmo tempo. Isso é útil quando você precisa acessar o índice do elemento durante a iteração.
# Exemplo de uso da função enumerate com uma lista:
minha_lista = ['a', 'b', 'c', 'd']
for indice, valor in enumerate(minha_lista):
    print(f"Índice: {indice}, Valor: {valor}")
# A função enumerate também aceita um segundo argumento opcional, que é o valor inicial do índice. Por padrão, o índice começa em 0, mas você pode especificar um valor diferente se desejar.
# Exemplo de uso da função enumerate com um valor inicial diferente:
minha_lista = ['a', 'b', 'c', 'd']
for indice, valor in enumerate(minha_lista, start=1):
    print(f"Índice: {indice}, Valor: {valor}")