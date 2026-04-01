import json

class Carro:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia

    @staticmethod
    def salva_carros(*carros):
        dicionario = dict()
        for carro in carros:
            dicionario[carro.nome] = carro.potencia
        texto = json.dumps(dicionario, indent=4)
        with open('carros.json', 'w') as arquivo:
            arquivo.write(texto)
    @staticmethod
    def le_carros():
        lista = []
        texto = None
        with open('carros.json', 'r') as arquivo:
            texto = arquivo.read()
        dicionario = json.loads(texto)
        for chave in dicionario:
            carro = Carro(chave, dicionario[chave])
            lista.append(carro)
        return lista
carro1 = Carro('Fusca', 50)
carro2 = Carro('Gol', 100)
Carro.salva_carros(carro1, carro2)
carros = Carro.le_carros()
for carro in carros:
    print(f'Carro: {carro.nome}, Potência: {carro.potencia} cavalos')
