# Funções iteráveis: generators
# Em Python, as funções iteráveis, também conhecidas como generators, são uma maneira eficiente de criar iteradores. Elas permitem que você gere uma sequência de valores sob demanda, em vez de armazenar toda a sequência na memória de uma vez. Isso é especialmente útil quando você está lidando com grandes conjuntos de dados ou sequências infinitas.
# Para criar um generator, você pode usar a palavra-chave yield em vez de return. Ao chamar uma função generator, ela retorna um objeto generator, que é um iterador. Cada vez que o método __next__() é chamado no generator, a função é executada até encontrar a próxima declaração yield, que retorna o valor especificado. O estado da função é mantido entre as chamadas, permitindo que ela continue de onde parou na próxima vez que for chamada.
# Exemplo de uma função generator que gera os números de 1 a 3:
def ancora():
    yield 1 # A palavra-chave yield é usada para gerar um valor e pausar a execução da função. O próximo valor será gerado na próxima chamada do generator.
    yield 2 # Cada vez que a função generator é chamada, ela continua a execução a partir da última declaração yield, permitindo que você gere uma sequência de valores de forma eficiente.
    yield 3 # Quando a função generator é chamada, ela retorna um objeto generator, que é um iterador. Você pode usar um loop for para percorrer os valores gerados pelo generator, ou chamar o método __next__() diretamente para obter o próximo valor.

for item in ancora():
    print(item)