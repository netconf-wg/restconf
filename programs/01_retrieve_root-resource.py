import requests
import json

device = json.loads(open("device_login.json").read())
url = f"https://{device['host']}/restconf"

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=device['headers'], auth=(device['username'], device['password']), verify=False).json()

print(response)
