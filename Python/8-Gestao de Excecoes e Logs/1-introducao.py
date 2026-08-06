# Introdução a Gestão de Exceções

try:
    ...
    # nesse bloco pode ocorrer erro
except: # pode haver mais uma cláusula
    ...
    # este bloco é executado em caso de erro
else: # opcional
    ...
    # executa somente se não houver erro
finally: # opcional
    ...
    # sempre será executada, com ou sem erro