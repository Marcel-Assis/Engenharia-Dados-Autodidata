# Parâmetros de execução

import sys

if(__name__=='__main__'):
    print(sys.__name__)

import teste
if(__name__=='__main__'):
    print(teste.__file__)

if(__name__=='__main__'):
    print(__name__)

if(__name__=='__main__'):
    exit(1)

if(__name__=='__main__'):
    print('Números de argumentos é', len(sys.argv))
    print("Argumento são ", sys.argv)
