import requests
import json

device = json.loads(open("device_login.json").read())
module = 'Cisco-IOS-XE-native:native/hostname'
url = f"https://{device['host']}/restconf/data/{module}"
payload = json.dumps({"Cisco-IOS-XE-native:hostname": "csr1000v-1"})

requests.packages.urllib3.disable_warnings()
response_put = requests.put(url, headers=device['headers'], auth=(device['username'], device['password']),
                            verify=False, data=payload)

response_get = requests.get(url, headers=device['headers'], auth=(device['username'], device['password']),
                            verify=False).json()

print(f"Current hostname is : {response_get['Cisco-IOS-XE-native:hostname']}")
