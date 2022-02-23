import requests
import json

device = json.loads(open("device_login.json").read())
module = 'ietf-yang-library:modules-state'
url = f"https://{device['host']}/restconf/data/{module}"


requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=device['headers'], verify=False,
                        auth=(device['username'], device['password'])).json()

# saving the Schema name and schema details in a file
schema_dict = {}
for schema in response['ietf-yang-library:modules-state']['module']:
    schema_dict[schema["name"]] = schema['schema']

with open("schema_list.json", 'w') as file:
    file.write(json.dumps(schema_dict))
