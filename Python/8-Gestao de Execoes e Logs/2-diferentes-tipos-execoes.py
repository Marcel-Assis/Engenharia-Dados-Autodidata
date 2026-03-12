print('Inicio')
lista = [1, 2, 3]
numero = 0
try:
    divisao = 10 / numero
except ZeroDivisionError as error1: # Captura o erro específico de divisão por zero
    print(f"Erro de divisão por zero: {error1}")
except IndexError as error2: # Captura o erro específico de índice fora do alcance
    print(f"Erro de índice: {error2}")
except Exception as error3: # Captura qualquer outro erro genérico que não foi tratado pelos excepts anteriores
    print(f"Erro genérico: {error3}")
print('Fim')