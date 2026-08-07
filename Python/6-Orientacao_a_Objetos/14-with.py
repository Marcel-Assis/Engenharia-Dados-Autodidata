# Usando o gerenciador de contexto "with" em Python

class Lista():
    def __init__(self): 
        pass
    
    def __enter__(self): # Método chamado ao entrar no contexto
        print('memória iniciada')
        self.lista = [i for i in range(0,10)]
        return self.lista

    def __exit__(self, *args, **kwargs): # Método chamado ao sair do contexto
        print('memória liberada')
        del self.lista

with Lista() as temp_lista: # Usando o gerenciador de contexto "with"
    for i in temp_lista:
        print(i)

print('Aqui o objeto não existe mais')