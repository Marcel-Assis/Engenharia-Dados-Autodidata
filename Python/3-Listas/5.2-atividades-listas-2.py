'''6 - Escolha três objetos de sua escolha e em seguida cria uma lista para
armazenar o objeto e sua função. Agora por input receba o nome desse objeto e
imprima a sua função. Caso o objeto não exista, informa ao usuário.'''
nome_input = input("Digite o nome do objeto: ")
objetos = {
    "celular": "comunicação e entretenimento",
    "computador": "trabalho e jogos",
    "carro": "transporte"
}
if nome_input in objetos:
    print(f"A função do {nome_input} é: {objetos[nome_input]}")
else:
    print("Objeto não encontrado.")


'''7 - Crie uma lista contendo todos os números negativos de -30 até -20. Printe
essa lista.'''
lista_negativos = [x for x in range(-30, -19) if x < 0]
print(lista_negativos)

'''8 - Percorra os números de 4 a 100 e mantenha apenas aqueles divisíveis por 4.'''
num_divididos_quatro = [x for x in range(4, 101) if x % 4 == 0]
print(num_divididos_quatro)

'''9 (DESAFIO) - Crie uma lista contendo todos os números de 0 a 100, mas filtre,
mantendo apenas os números que terminam com 0.'''
numeros_terminados_em_zero = [x for x in range(101) if x % 10 == 0]
print(numeros_terminados_em_zero)

'''10 - Percorra os números de 0 a 20 e crie um array, onde caso o número terminar
com zero o valor devera ser '0', caso contrario devera ser '-'.'''
array = ['0' if x % 10 == 0 else '-' for x in range(21)]
print(array)
