print('Inicio')
lista = [1,2,3]
try: # Código que pode dar erro
    print(f'Try: {lista[10]}')
except Exception as error: # Código executado se der erro
    print(f"Except: Ocorreu um erro: {error}")
else: # Código executado se não der erro - opcional
    print("Else: Nenhum erro ocorreu.")
finally: # Código executado sempre - opcional
    print("Finally: Fim do bloco try-except")
print('Fim')