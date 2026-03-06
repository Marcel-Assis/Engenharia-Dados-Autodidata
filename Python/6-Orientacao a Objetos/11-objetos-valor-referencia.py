# Objetos em Python: valor vs referência
# Em Python, variáveis são referências para objetos na memória. Isso significa que quando você atribui um objeto a uma variável, você está criando uma referência para esse objeto, não uma cópia dele.

# Exemplo:
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Saída: [1, 2, 3, 4]

# Isso acontece porque tanto 'a' quanto 'b' referenciam o mesmo objeto na memória.

# Se quisermos criar uma cópia independente, podemos usar o método copy():
c = a.copy()
c.append(5)
print(a)  # Saída: [1, 2, 3, 4]
print(c)  # Saída: [1, 2, 3, 4, 5]