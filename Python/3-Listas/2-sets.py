# Sets:

# Criar um set:
meu_set = {1, 2, 3, 4, 5}

# Adicionar elementos:
meu_set.add(6)

# Remover elementos:
meu_set.remove(3)  # Remove o elemento 3
meu_set.discard(10)  # Remove o elemento 10 se existir, caso contrário não faz nada

# Operações com sets:
outro_set = {4, 5, 6, 7, 8}
uniao = meu_set | outro_set  # União
uniao2 = meu_set.union(outro_set)  # União
intersecao = meu_set & outro_set  # Interseção
intersecao2 = meu_set.intersection(outro_set)  # Interseção
diferenca = meu_set - outro_set  # Diferença
diferenca2 = meu_set.difference(outro_set)  # Diferença
diferenca_simetrica = meu_set ^ outro_set  # Diferença simétrica
diferenca_simetrica2 = meu_set.symmetric_difference(outro_set)  # Diferença simétrica

# Verificar se um elemento está no set:
existe = 4 in meu_set  # True

