'''1 - Crie um programa que diga “se você precisar ir ao
mercado”. Você precisa ir ao mercado se “faltar comida” ou
“se for sábado”. Mostre na saída do programa o valor
lógico, indicando sim ou não.'''

faltar_comida = True
sabado = False

precisa_ir_mercado = faltar_comida or sabado
print('Você precisa ir ao mercado?', precisa_ir_mercado)

'''2 - Crie um programa que responda “se você pode atravessar
a rua” na faixa de pedestres. Você pode atravessar a rua
se o “sinal estiver vermelho” e “se não houver nenhum
carro vindo da direita” E “nem da esquerda”. Altere as
variáveis para verificar se o programa esta correto.
Mostre na saída do programa o valor lógico.'''
sinal_vermelho = True
carro_direita = False
carro_esquerda = False
pode_atravessar = sinal_vermelho and not carro_direita and not carro_esquerda
print('Você pode atravessar a rua?', pode_atravessar)

'''3 - Agora faça a mesma coisa que o exercício anterior, mas
desta vez você esta com pressa e para atravessar a rua
basta que o sinal esteja vermelho “OU” que não venha carro
da esquerda e direita. Altere as variáveis para verificar
a resposta em comparação com ao exercício anterior. Mostre
na saída do programa o valor lógico.'''
pode_atravessar_com_pressa = sinal_vermelho or not carro_direita and not carro_esquerda
print('Você pode atravessar a rua com pressa?', pode_atravessar_com_pressa)