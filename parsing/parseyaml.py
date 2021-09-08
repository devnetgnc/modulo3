# Fill in this file with the code from parsing YAML exercise
import json


import json
import yaml
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)
    print(ouryaml)
    print("El token de acceso es {}".format(ouryaml['access_token']))
    print("El token expira en {} segundos".format(ouryaml['expires_in']))
    print('\n\n')
    print(json.dumps(ouryaml, indent=4))