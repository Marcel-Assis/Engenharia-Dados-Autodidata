# Uso básico de módulos em Python
# Explicação: Módulos são arquivos que contêm definições e instruções em Python. Eles permitem organizar o código em partes reutilizáveis e facilitam a manutenção. Para usar um módulo, utilizamos a palavra-chave `import` seguida do nome do módulo. Por exemplo, o módulo `math` fornece funções matemáticas como `sqrt` (raiz quadrada) e constantes como `pi`.

import math

print(math.sqrt(16))
print(math.pi)

# Explicação: O módulo `math` é um exemplo de módulo embutido em Python. Ele fornece várias funções matemáticas e constantes que podem ser usadas diretamente após a importação.
# Outros exemplos de módulos embutidos incluem `os` para operações do sistema operacional, `sys` para manipulação de variáveis e funções do interpretador, e `random` para geração de números aleatórios.

print(dir(math)) # Lista todos os atributos e métodos disponíveis no módulo math
print(dir(math.pi)) # Lista os atributos e métodos disponíveis para o objeto math.pi
print(math.__name__) # Exibe o nome do módulo
print(math.__file__) # Exibe o caminho do arquivo do módulo
print(math.__doc__) # Exibe a documentação do módulo math
