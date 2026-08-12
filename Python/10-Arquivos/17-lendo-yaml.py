# Lendo Formato Yaml

import yaml
with open('exemplo_config.yaml') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
    dtname = data['database']['name']
    dtcloud = data['cloud']['provider']
print(dtname)
print(dtcloud)