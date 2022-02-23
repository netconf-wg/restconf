import requests
import json

device = json.loads(open("device_login.json").read())
int_conf_module = 'ietf-interfaces:interfaces'
int_state_module = 'ietf-interfaces:interfaces-state'
url = f"https://{device['host']}/restconf/data/"

requests.packages.urllib3.disable_warnings()
interface_config = requests.get(f"{url}{int_conf_module}", headers=device['headers'],
                                auth=(device['username'], device['password']), verify=False).json()
interface_state = requests.get(f"{url}{int_state_module}", headers=device['headers'],
                               auth=(device['username'], device['password']), verify=False).json()

print("\nBelow are interfaces details :\n")
for int_config, int_state in zip(interface_config['ietf-interfaces:interfaces']['interface'],
                                 interface_state['ietf-interfaces:interfaces-state']['interface']):
    print(f"Name : {int_config['name']}")
    if 'description' in int_config.keys():
        print(f"Description : {int_config['description']}")
    print(f"Type : {int_config['type']}")
    if bool(int_config['ietf-ip:ipv4']):
        for i in range(0, len(int_config['ietf-ip:ipv4']['address'])):
            print(f"IP Address : {int_config['ietf-ip:ipv4']['address'][i]['ip']}")
            print(f"Subnet Mask : {int_config['ietf-ip:ipv4']['address'][i]['netmask']}")
    print(f"MAC Address : {int_state['phys-address']}")
    print(f"Incoming packets : {int_state['statistics']['in-unicast-pkts']}")
    print(f"Outgoing packets : {int_state['statistics']['out-unicast-pkts']}")
    print("------------------------------------------------------------")
