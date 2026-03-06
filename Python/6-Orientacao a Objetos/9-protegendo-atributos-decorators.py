# Protegendo atributos usando decorators

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome # atributo privado

    @property
    def nome(self): # método getter
        print('pegando nome')
        return self.__nome
    
    @nome.setter
    def nome(self, valor): # método setter
        print('alterando nome')
        self.__nome = valor

instancia = Pessoa('Maria') # criando instância
print(instancia.nome)
instancia.nome = 'João' # alterando nome
print(instancia.nome)