'''1 - Crie um programa que possui uma variável
do “tipo string” contendo um número que
indique quanto você tem no banco. Em seguida
desconte mil deste valor e mostre na saída do
programa.'''
saldo_str = '5000'
saldo_float = float(saldo_str)
saldo_float -= 1000
print('Saldo após o desconto de mil:', saldo_float)
'''2 - Crie um programa que indique se seu saldo
bancário esta zerado (valor lógico). Declare
uma variável para guardar seu saldo bancário.'''
saldo_bancario = 4000.4
esta_zerado = not bool(saldo_bancario)
print('Seu saldo bancário está zerado?', esta_zerado)
'''3 - Crie um programa que contenha sua altura,
mas deve somente mostrar a parte inteira de
sua altura na saída do programa, pois queremos
uma estimativa.'''
altura = 1.81
altura_inteira = int(altura)
print('Sua altura aproximada é', altura_inteira)