import csv
### O módulo csv é uma biblioteca padrão do Python que fornece funcionalidades para ler e escrever arquivos CSV (Comma-Separated Values). Ele facilita a manipulação de dados tabulares, permitindo que você trabalhe com arquivos CSV de forma eficiente e fácil. Para criar um arquivo CSV usando o módulo csv, você pode seguir os seguintes passos:
with open("pessoas.csv", "w") as arquivo:
    escritorCsv = csv.writer(arquivo, delimiter=",") # Criar um objeto escritorCsv usando a função csv.writer() para escrever no arquivo "pessoas.csv". O parâmetro delimiter="," especifica que o delimitador entre os campos será uma vírgula.
    escritorCsv.writerow(["id", "nome", "profissão"]) # Usar o método writerow() do objeto escritorCsv para escrever uma linha no arquivo CSV. Esta linha contém os cabeçalhos das colunas: "id", "nome" e "profissão". Cada elemento da lista passada para writerow() representa um campo na linha do arquivo CSV.
    escritorCsv.writerow([1, "João", "Engenheiro"]) # Usar o método writerow() novamente para escrever outra linha no arquivo CSV. Esta linha contém os dados de uma pessoa: id 1, nome "João" e profissão "Engenheiro". Cada elemento da lista passada para writerow() representa um campo na linha do arquivo CSV.
    escritorCsv.writerow([2, "Maria", "Médica"]) # Usar o método writerow() novamente para escrever mais uma linha no arquivo CSV. Esta linha contém os dados de outra pessoa: id 2, nome "Maria" e profissão "Médica". Cada elemento da lista passada para writerow() representa um campo na linha do arquivo CSV.
    escritorCsv.writerow([3, "Pedro", "Professor"]) # Usar o método writerow() novamente para escrever mais uma linha no arquivo CSV. Esta linha contém os dados de outra pessoa: id 3, nome "Pedro" e profissão "Professor". Cada elemento da lista passada para writerow() representa um campo na linha do arquivo CSV.
    print("Arquivo CSV criado com sucesso.") # Imprimir uma mensagem indicando que o arquivo CSV foi criado com sucesso


### Outra forma de escrever um arquivo CSV é usando o método writerows(), que permite escrever várias linhas de uma só vez. Para isso, podemos organizar os dados em uma estrutura de lista de listas, onde cada sublista representa uma linha a ser escrita no arquivo CSV. A seguir, um exemplo de como usar o método writerows() para criar um arquivo CSV com as mesmas informações do exemplo anterior:
linhas = [
    ["id", "nome", "profissão"],
    [1, "João", "Engenheiro"],
    [2, "Maria", "Médica"],
    [3, "Pedro", "Professor"]
]
with open("pessoas2.csv", "w") as file:
    escritorCsv = csv.writer(file, delimiter=",") # Criar um objeto escritorCsv usando a função csv.writer() para escrever no arquivo "pessoas2.csv". O parâmetro delimiter="," especifica que o delimitador entre os campos será uma vírgula.
    escritorCsv.writerows(linhas) # Usar o método writerows() do objeto escritorCsv para escrever várias linhas no arquivo CSV de uma só vez. O método writerows() recebe uma lista de listas, onde cada sublista representa uma linha a ser escrita no arquivo CSV. Neste caso, a variável linhas contém as mesmas informações que foram escritas anteriormente, mas agora estão organizadas em uma estrutura de lista de listas.
    print("Arquivo CSV criado com sucesso.") # Imprimir uma mensagem indicando que o arquivo CSV foi criado com sucesso

with open("pessoas2.csv", "r") as file:
    leitorCsv = csv.reader(file, delimiter=",") # Criar um objeto leitorCsv usando a função csv.reader() para ler o arquivo "pessoas2.csv". O parâmetro delimiter="," especifica que o delimitador entre os campos é uma vírgula.
    for linha in leitorCsv: # Usar um loop for para iterar sobre cada linha do arquivo CSV lido pelo objeto leitorCsv. Cada linha é representada por uma lista de campos, onde cada campo corresponde a um elemento da lista.
        print(linha) # Imprimir a linha atual do arquivo CSV. Cada linha será exibida como uma lista de campos, onde cada campo é um elemento da lista.