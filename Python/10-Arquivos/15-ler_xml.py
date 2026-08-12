# Lendo XML

import xml.etree.ElementTree as xml

tree = xml.parse('dados_pessoais_3.xml')
root = tree.getroot() #método pra acessar a raíz do arquivo
print(root.tag)
for pessoa in root:
    print(' ', pessoa.tag, pessoa.attrib['Nome'])
    for dado in pessoa:
        if (dado.tag == 'filhos'):
            for filho in dado:
                print('    ', filho.tag, filho.attrib['nome'])
        else:
            print('    ', dado.tag, dado.text)