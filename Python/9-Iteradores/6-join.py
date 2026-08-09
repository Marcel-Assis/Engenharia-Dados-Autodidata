# Join de Iteradores

# A função join pode ser usada pra juntar objetos iteráveis

# Exemplo

texto1 = 'olá'
print("#".join(texto1)) # pra cada elemento do texto1 ele juntou o hashtag


lista = ['a', 'b', 'c', 'd']
letras = ' '.join(lista)
print(letras) # adicionou um espaço pra cada letra da lista

letras2 = '-'.join([str(i) for i in range(10)])
print(letras2) # adicionou um traço pra cada elemento percorrido em range

def anos():
    for i in range(2020, 2030):
        yield str(i)

letras3 = '-'.join(anos())
print(letras3) # adicionou traços aos anos percorridos da função

