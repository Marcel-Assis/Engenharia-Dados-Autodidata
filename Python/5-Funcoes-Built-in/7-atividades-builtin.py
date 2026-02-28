'''6 - Crie uma função que receba uma string e uma letra do alfabeto. Retorne a quantidade de vezes
que essa letra tem na string. Caso não ocorra nenhuma vez, retorne 0.'''
def contadorLetra(texto, letra):
    return texto.count(letra)
print(contadorLetra('Marcel', 't'))

'''7 (DESAFIO) - Crie uma função que receba uma string e uma letra do alfabeto. Retorne uma lista
contendo o índice de onde todas as ocorrências aparecem.'''
def indiceLista(texto, letra):
    lista = []
    indice = 0
    for char in texto:
        if char == letra:
            lista.append(indice)
        indice += 1
    return lista
print(indiceLista('Marcel Assis', 's'))

'''8 - Crie uma função que receba o que foi digitado pelo usuário no chat e também uma lista
contendo todas as palavras não permitidas a serem digitadas. Essa função então retornara o
que foi digitado pelo usuário mas no lugar das palavras não permitidas retorna o caractere '*'.'''
palavrasNaoPermitidas = ['diabo', 'droga']
textoUsuario = 'Não pode falar diabo nem droga no chat'
def retiraPalavras(texto, palavras):
    for palavra in palavras:
        if palavra in texto:
            texto = texto.replace(palavra, '*')
    return texto
print(retiraPalavras(textoUsuario, palavrasNaoPermitidas))

'''9 - Crie uma função que retorne verdadeiro se uma string é totalmente maiúscula ou
totalmente minúscula.'''
def maiusculaOuMinuscula(texto):
    return texto.isupper() or texto.islower()
print(maiusculaOuMinuscula('TESTE'))

'''10 - Crie uma função que receba uma lista de textos. Detecte quais os valores dessa lista são
inteiros e em seguida transforme eles para um número do tipo inteiro. Todos esses valores
encontrados serão retornados em uma nova lista que deve estar ordenada.'''
