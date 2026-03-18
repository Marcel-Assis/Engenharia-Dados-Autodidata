# Join de iteradores é uma técnica que permite combinar múltiplos iteradores em um único iterador. Isso é útil quando você deseja iterar sobre vários iteradores de forma sequencial, sem precisar criar uma lista intermediária.

# O método join() é uma função de string que pode ser usada para juntar os elementos de um iterador em uma única string, usando um separador especificado. O iterador deve conter apenas strings, caso contrário, será necessário converter os elementos para strings antes de usar join().
texto1 = "Olá"
print("#".join(texto1))  # O#l#á

lista = ['a', 'b', 'c', 'd']
letras = ' '.join(lista) # Juntando os elementos da lista com um espaço entre eles
print(letras)  # a b c d

letras = '-'.join([str(i) for i in range(10)]) # Gerando uma lista de strings a partir de um iterador de números e depois juntando com '-'
print(letras)  # 0-1-2-3-4-5-6-7-8-9

def anos():
    for ano in range(2000, 2021):
        yield str(ano)  # Gerando anos como strings

letras = '-'.join(anos())  # Juntando os anos gerados pelo iterador com ', ' como separador
print(letras)  # 2000-2001-2002-2003-2004-2005-2006-2007-2008-2009-2010-2011-2012-2013-2014-2015-2016-2017-2018-2019-2020