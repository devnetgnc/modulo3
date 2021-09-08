# Fill in this file with the code from parsing JSON exercise
import json
import yaml
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
    print(ourjson)
    print('el token de acceso es:{}'.format(ourjson['access_token']))
    print('el token expira en:{} segundos'.format(ourjson['expires_in']))