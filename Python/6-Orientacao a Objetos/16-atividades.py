'''1 - Crie uma classe para representar um carro. Ele deve ter um atributo
que diga sua potência em cavalos. Outro atributo deve dizer quanto de
gasolina por quilômetros ele consome. Cria duas instâncias e mostre os
valores.
Exemplo saída:
Potência do carro 1: 100 cavalos
Alcance do carro 1: 200 km/l
Potência do carro 2: 200 cavalos
Alcance do carro 2: 350.5 km/l'''
class Carro():
    def __init__(self, potencia, gasolina):
        self.potencia = potencia
        self.gasolina = gasolina
carro1 = Carro(100, 200)
carro2 = Carro(200, 350.5)
print(f'Potência do carro 1: {carro1.potencia} cavalos')
print(f'Alcance do carro 1: {carro1.gasolina} km/l')
print(f'Potência do carro 2: {carro1.potencia} cavalos')
print(f'Alcance do carro 2: {carro1.gasolina} km/l')

'''2 - Cria uma classe que represente uma pessoa. Ela deve possuir um
nome, CPF e um dependente, onde o dependente é outra pessoa.
Dependente não é obrigatório. Crie duas instâncias: pai e filho, e imprima
as saídas.
Exemplo saída:
Nome: Rodrigo CPF: 200.300.400-45 Dependente: None
Nome: Fernando CPF: 100.200.300-45 Dependente: Rodrigo'''
class Pessoa():
    def __init__(self, nome, cpf, dependente=None):
        self.nome = nome
        self.cpf = cpf
        self.dependente = dependente
filho = Pessoa('Fernando', '100.200.300-45')
pai = Pessoa('Rodrigo', '200.300.400-45', filho.nome)
print(f'Nome: {filho.nome} CPF: {filho.cpf} Dependente: {filho.dependente}')
print(f'Nome: {pai.nome} CPF: {pai.cpf} Dependente: {pai.dependente}')

'''3 - Crie uma classe base que represente um veículo. Os atributos devem
ser peso do veiculo, número de rodas e potência. Em seguida crie três
classes que herdam esse veículo: ônibus, carro e moto. Crie uma instância
de cada tipo e imprima as instâncias
Ônibus: Peso 1000 Potência 400 Rodas 6
Carro: Peso 300 Potência 100 Rodas 4
Moto: Peso 100 Potência 50 Rodas 2'''
class Veiculo():
    def __init__(self, peso, num_rodas, potencia):
        self.peso = peso
        self.num_rodas = num_rodas
        self.potencia = potencia
    def distanciaPercorrida(self):
        return self.peso / self.potencia * 1000
    def __lt__(self, outro): # Sobrescrevi o método <
        return self.potencia < outro.potencia
    def __gt__(self, outro): # Sobrescrevi o método >
        return self.potencia > outro.potencia
class Onibus(Veiculo):
    def __init__(self, peso, num_rodas, potencia):
        Veiculo.__init__(self, peso, num_rodas, potencia) # Sobrescrevi o método init usando a classe base Veiculo (precisa adicionar o self também)
class Carro(Veiculo):
    def __init__(self, peso, num_rodas, potencia):
        super().__init__(peso, num_rodas, potencia) # Sobrescrevi o método init usando a classe base Veiculo porém utilizando o super
class Moto(Veiculo):
    pass # Não sobrescrevi o método init
onibus = Onibus(1000, 6, 400)
carro = Carro(300, 4, 100)
moto = Moto(100, 2, 50)
print(f'Ônibus: Peso {onibus.peso} Potência {onibus.potencia} Rodas {onibus.num_rodas}')
print(f'Carro: Peso {carro.peso} Potência {carro.potencia} Rodas {carro.num_rodas}')
print(f'Moto: Peso {moto.peso} Potência {moto.potencia} Rodas {moto.num_rodas}')

'''4 - Baseado no exercício anterior, cria uma função na classe base que diga
a distância percorrida. Vamos supor que esse valor é dado pela peso do
veículo dividido pela potência do veículo vezes mil. Crie uma moto, carro e
um ônibus. Mostre esses valores.
Ex: (200 cavalos/ 400 cavalos) * 1000 = 500 quilômetros
Exemplo saída:
Distância percorrida ônibus: 2500.0
Distância percorrida carro: 3000.0
Distância percorrida moto: 2000.0'''
print(f'Distância percorrida ônibus: {onibus.distanciaPercorrida()}')
print(f'Distância percorrida carro: {carro.distanciaPercorrida()}')
print(f'Distância percorrida moto: {moto.distanciaPercorrida()}')

'''5 - Baseado no exercício anterior, crie os operador '>' e '<' para dizer qual veículo
é mais potente. Compare um de cada tipo.
Observação, sobrescreva os métodos __lt__ e __gt__'''
print(onibus > carro)
print(onibus < moto)
print(moto < carro)

'''6 - Cria uma classe que represente um número negativo, use propriedades
(@property) para controlar o valor guardado pela classe, sem deixar que ele
fique positivo (0 pode). Além disso crie alguns operadores para comparação e de subtração. Cuide para que nenhum valor positivo surja.'''
class Negativo():
    def __init__(self, numero):
        self.__numero = numero
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if valor <= 0:
            self.__numero = valor
    def __sub__(self, outro):
        sub = self.__numero - outro
        if sub > 0:
            sub = 0
        return sub
    def __lt__(self, outro):
        return self.__numero < outro
    def __gt__(self, outro):
        return self.__numero > outro
negativo = Negativo(-3)
print(negativo < 3)
print(negativo > 3)
negativo.numero = -4
print(negativo.numero)
print(negativo.numero - 10)

'''7 - Cria uma função que diga se um objeto é um primitivo do Python, informando
que é sempre passado valor Ex: [int, float, str, bool], ou se é um objeto passado
por referência'''
def eh_primitivo(objeto):
    if isinstance(objeto, (int, float, str, bool)):
        return 'É um objeto passado valor'
    else:
        return 'É um objeto passado por referência'
    
print(eh_primitivo(True))
print(eh_primitivo(Negativo))