# Dicionários:

# Criar um dicionário:
meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Acessar valores:
print(meu_dicionario["nome"])  # Alice
print(meu_dicionario.get("idade"))  # 25
idade = meu_dicionario.get("idade", "Não informado")  # Retorna "Não informado" se a chave não existir

# Adicionar ou atualizar valores:
meu_dicionario["idade"] = 26  # Atualiza a idade
meu_dicionario.update({"idade": 26})  # Atualiza a idade
meu_dicionario["profissao"] = "Engenheira"  # Adiciona uma nova chave

# Remover valores:
del meu_dicionario["cidade"]  # Remove a chave "cidade"
valor_removido = meu_dicionario.pop("idade")  # Remove a chave "idade" e retorna o valor
meu_dicionario.popitem()  # Remove o último item inserido

# Operações com dicionários:
chaves = meu_dicionario.keys()  # Retorna as chaves
valores = meu_dicionario.values()  # Retorna os valores
itens = meu_dicionario.items()  # Retorna os itens (chave, valor)

# Verificar se uma chave está no dicionário:
existe = "nome" in meu_dicionario  # True

# Percorrendo dicionários com for:
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# Percorrendo apenas as chaves:
for chave in meu_dicionario.keys():
    print(chave)

# Percorrendo apenas os valores:
for valor in meu_dicionario.values():
    print(valor)

# Contar elementos em um dicionário:
quantidade = len(meu_dicionario)  # Retorna o número de elementos no dicionário

# Contar chaves específicas:
quantidade_nomes = list(meu_dicionario.keys()).count("nome")  # Retorna o número de vezes que a chave "nome" aparece

# Contar valores específicos:
quantidade_idade_20 = list(meu_dicionario.values()).count(20)  # Retorna o número de vezes que o valor "20" aparece

# Dicionários dentro de dicionários:
meu_dicionario_aninhado = {
    "pessoa1": {"nome": "Alice", "idade": 25},
    "pessoa2": {"nome": "Bob", "idade": 30},
}

# Acessando valores em dicionários aninhados:
nome_pessoa1 = meu_dicionario_aninhado["pessoa1"]["nome"]  # Alice
idade_pessoa2 = meu_dicionario_aninhado["pessoa2"]["idade"]  # 30

# Adicionando valores em dicionários aninhados:
meu_dicionario_aninhado["pessoa1"]["profissao"] = "Engenheira"  # Adiciona uma nova chave ao dicionário aninhado

# Removendo valores em dicionários aninhados:
del meu_dicionario_aninhado["pessoa1"]["profissao"]  # Remove a chave "profissao" do dicionário aninhado

# Percorrendo dicionários aninhados:
print("------")
for pessoa, info in meu_dicionario_aninhado.items():
    print(f"{pessoa}:")
    for chave, valor in info.items():
        print(f"  {chave}: {valor}")

