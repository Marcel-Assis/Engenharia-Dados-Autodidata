# Protegendo atributos usando property

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome # atributo privado

    def get_nome(self): # método getter
        print('pegando nome')
        return self.__nome
    
    def set_nome(self, valor): # método setter
        print('alterando nome')
        self.__nome = valor
    
    nome = property(get_nome, set_nome) # criando propriedades get e setter
    #nome = property(fset = set_nome) # criando propriedade somente com setter
    #fset para definir o método setter
    #fget para definir o método getter
    #fdel para definir o método deleter

instancia = Pessoa('Maria') # criando instância
print(instancia.nome)
instancia.nome = 'João' # alterando nome
print(instancia.nome)