import teste
print(dir(teste))
print(teste.PI)
var = teste.Teste()
teste.MyFunc(10)

from teste import PI
print(PI)

from teste import PI as NUMERO_PI
print(NUMERO_PI)

from teste import MyFunc
MyFunc("Teste")