# Criando um Objeto Iterável

class ColecaoNumeros:
    def __init__(self, numero_max): # Método de inicialização padrão da classe
        self.max = numero_max # Quando iniciar a classe vamos definir o número máximo que ela vai iterar

    def __iter__(self): # O método iter vai ser chamado implicitamente na inicialização da classe
        self.numero_atual = 0 # Quando a classe for inicializada vamos definir o primeiro número que será percorrido no laço (pra começar no 0, colocar 0, pra começar no 1, colocar 1)
        return self

    def __next__(self): # O método next vai retornar o próximo número (será chamado sempre que chamar um laço for ou chamar a função next)
        if self.numero_atual <= self.max: # Vai verificar se o número atual é menor ou igual ao numero max definido ao instanciar a classe
            retorno = self.numero_atual
            self.numero_atual += 1
            return retorno
        else: # Se não for, vai gerar uma exceção
            raise StopIteration

colecao = ColecaoNumeros(6) # Instancia a classe e define o número max de iteração

# Utilizando o for
for item in colecao: # Percorre até o número max (definido ao instanciar)
    print(item)

# Utilizando o iter com next (pois a classe tem o __iter__)
iterador = iter(colecao)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
