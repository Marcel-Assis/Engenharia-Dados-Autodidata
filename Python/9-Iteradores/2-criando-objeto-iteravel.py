class ColecaoNumeros: # Criando uma classe que representa uma coleção de números
    def __init__(self, numero_max): # O método __init__ é o construtor da classe, que é chamado quando um objeto é criado. Ele recebe um parâmetro numero_max, que define o número máximo da coleção.
        self.max = numero_max # Atributo que armazena o número máximo da coleção
    def __iter__(self): # O método __iter__ é chamado quando um iterador é criado a partir do objeto. Ele deve retornar um objeto iterador, que é responsável por percorrer os elementos da coleção.
        self.numero_atual = 0 # Atributo que armazena o número atual da coleção, que começa em 0
        return self # Retorna o próprio objeto como iterador, pois ele implementa o método __next__
    def __next__(self): # O método __next__ é chamado para obter o próximo elemento da coleção. Ele deve retornar o próximo elemento ou lançar a exceção StopIteration quando não houver mais elementos para percorrer.
        if self.numero_atual <= self.max: # Verifica se o número atual é menor ou igual ao número máximo da coleção
            retorno = self.numero_atual # Armazena o número atual em uma variável de retorno
            self.numero_atual += 1 # Incrementa o número atual para o próximo elemento da coleção
            return retorno # Retorna o número atual antes de incrementá-lo
        else: # Se o número atual for maior que o número máximo da coleção, significa que não há mais elementos para percorrer
            raise StopIteration # Lança a exceção StopIteration para indicar que o iterador atingiu o final da coleção
        
# Criando um objeto iterável
colecao = ColecaoNumeros(5)
# Usando o iterador para percorrer os números da coleção
for numero in colecao:
    print(numero) 