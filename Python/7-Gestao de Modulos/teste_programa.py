import sys

if (__name__ == '__main__'):
    if len(sys.argv) != 3:
        print('Números de argumentos incorretos')
        sys.exit(1)
    numero1 = float(sys.argv[1])
    numero2 = float(sys.argv[2])
    print(numero1 + numero2)
