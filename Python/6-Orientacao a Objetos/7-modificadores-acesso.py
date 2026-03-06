# Modificadores de acesso em Python

class MinhaClasse:
    def __init__(self):
        # Atributos
        self.publico = "Atributo público"
        self._protegido = "Atributo protegido"
        self.__privado = "Atributo privado"

    # Funções privadas
    def __funcao_privada(self):
        print("Função privada")

obj = MinhaClasse()
print(obj.publico)       # Acessível
print(obj._protegido)    # Acessível, mas não recomendado
# print(obj.__privado)   # Não acessível diretamente
print(obj._MinhaClasse__privado)  # Acessível através do name mangling

# Funções privadas também podem ser acessadas através do name mangling
# obj.__funcao_privada()  # Não acessível diretamente
obj._MinhaClasse__funcao_privada()  # Acessível através do name mangling