import teste # Importação do módulo teste.py
print(dir(teste)) # Exibição dos atributos e métodos do módulo
print(teste.PI) # Acesso à constante PI do módulo
var = teste.Teste() # Criação de uma instância da classe Teste
teste.MyFunc(10) # Chamada da função MyFunc do módulo

from teste import PI # Importação da constante PI do módulo
print(PI) # Exibição da constante PI

from teste import PI as NUMERO_PI # Importação da constante PI com alias
print(NUMERO_PI) # Exibição da constante PI com alias

from teste import MyFunc # Importação da função do módulo
MyFunc("Teste") # Chamada da função MyFunc do módulo