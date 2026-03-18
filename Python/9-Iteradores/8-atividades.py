'''1 - Crie uma função iterável “meses” que retorne meses. Use um laço for para mostrar os
valores.'''
def meses():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for i in meses:
        yield i
for mes in meses():
    print(mes)

'''2 - Cria uma função iterável que receba uma lista de números e que
retorne a cada iteração um item dessa lista multiplicado por dois.'''
lista_num = [1, 2, 3, 4, 5]
def duplicado(lista):
    for i in lista:
        yield i*2
for x in duplicado(lista_num):
    print(x)

'''3 - Crie uma classe iterável chamada “Tabuada” que calcule a tabuada da
multiplicação do número recebido no construtor. A cada iteração ela
deve retornar um resultado da tabuada. Para testar use um laço for.'''
class Tabuada:
    def __init__(self, numero):
        self.numero = numero
    def __iter__(self):
        self.numero_atual = 0
        return self
    def __next__(self):
        if self.numero_atual <= 10:
            retorno = self.numero * self.numero_atual
            self.numero_atual += 1
            return retorno
        else:
            raise StopIteration
tabuada = Tabuada(5)
for numero in tabuada:
    print(numero)

'''4 (Desafio) - Crie uma classe que retorne os fatoriais de um número no
intervalo de X a Y, recebidos por parâmetro no construtor da classe.'''
class Fatorial:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __iter__(self):
        self.atual = self.x
        return self
    @staticmethod
    def calculaFatorial(num):
        result = 1
        for i in range(1, num+2):
            result *= i
        return result
    def __next__(self):
        if (self.atual == self.y + 1):
            raise StopIteration
        result = Fatorial.calculaFatorial(self.atual)
        self.atual += 1
        return result
for i in Fatorial(1, 10):
    print(i)

'''5 - Utilizando como base o exercício 1, retorne o número que representa
o mês e o próprio mês. Faça isso de duas maneiras diferentes (usando
enumeradores e a outra usando join).'''
def meses_enum():
    lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for i in enumerate(lista_meses):
        yield i
    
for indice, mes in meses_enum():
    print(indice+1, mes)

'''6 - Crie uma função que receba uma lista de frases e junte as mesmas em
uma só, separados por ponto final.'''
def frase(lista):
    return '. '.join(lista) + '.'

textos = ['Olá, sou Marcel', 'Gosto de Python', 'Trabalho como dev']
print(frase(textos))