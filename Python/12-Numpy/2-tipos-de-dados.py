# Tipos de Dados

import numpy

boolean = numpy.bool(True)
print(boolean)
print(type(boolean))

string = numpy.str_('este é um texto') #bytes_ caso não haja acento (ASCII)
print(string)
print(type(string))

# inteiro de 32 bits
inteiro = numpy.intc(-102)
print(inteiro, type(inteiro))
# inteiro de 32 bits sem sinal
uinteiro = numpy.uintc(102)
print(uinteiro, type(uinteiro))
# inteiro de 64 bits
long = numpy.int_(-84848484)
print(long, type(long))
# inteiro de 64 bits sem sinal
ulong = numpy.uint(34353434)
print(ulong, type(ulong))
