def printa_positivo(numero):
    if numero < 0:
        raise ValueError("O número deve ser positivo.") # Gerando uma exceção personalizada usando raise
    print(f"O número é: {numero}")

try:
    printa_positivo(-5)
except ValueError as error: # Captura a exceção personalizada ValueError
    print(f"Erro: {error}")
except Exception as error:
    print(f"Erro genérico: {error}")

# usando assert para validar uma condição e gerar uma exceção AssertionError se a condição for falsa
def valida_idade(idade):
    assert idade >= 18, "A idade deve ser maior ou igual a 18 anos." # Gerando uma exceção personalizada usando assert
    print(f"A idade é: {idade}")
try:
    valida_idade(16)
except AssertionError as error: # Captura a exceção personalizada AssertionError
    print(f"Erro de validação: {error}")
except Exception as error:
    print(f"Erro genérico: {error}")
