import teste
print(teste.__name__) # Nome do módulo

print(teste.__file__) # Caminho do arquivo do módulo

# Função que inicia o programa
def main():
    print("Aqui inicia o programa")
if __name__ == "__main__":
    main()

# Exemplo de uso de argumentos de linha de comando
import sys
if (__name__ == "__main__"):
    print("Número de argumentos:", len(sys.argv)) # Número de argumentos passados na linha de comando
    print("Argumentos:", sys.argv) # Lista de argumentos passados na linha de comando

if (__name__ == "__main__"):
    exit(0) # Encerra o programa com código de saída 0 (sucesso) ou 1 (erro)