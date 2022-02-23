import sys
import requests
import json

device = json.loads(open("device_login.json").read())
int_conf_module = 'ietf-interfaces:interfaces'
int_state_module = 'ietf-interfaces:interfaces-state'
url = f"https://{device['host']}/restconf/data/"
requests.packages.urllib3.disable_warnings()


def get_interface_list():
    config_response = requests.get(f"{url}{int_conf_module}", headers=device['headers'],
                                   auth=(device['username'], device['password']), verify=False).json()
    return config_response['ietf-interfaces:interfaces']['interface']


def get_interface_name(interface_list):
    intname = None
    while intname is None:
        int_name = input("\n Please enter the interface name : ")
        for intf_name in interface_list:
            if int_name.lower() == intf_name.lower():
                intname = intf_name
                break
        if intname is not None:
            return intname
        else:
            print("invalid interface / Enter the name in same format")
            continue


def get_interface_details(int_name):
    int_config = requests.get(f"{url}{int_conf_module}/interface={int_name}", headers=device['headers'],
                              auth=(device['username'], device['password']), verify=False).json()[
        'ietf-interfaces:interface']
    int_state = requests.get(f"{url}{int_state_module}/interface={int_name}", headers=device['headers'],
                             auth=(device['username'], device['password']), verify=False).json()[
        'ietf-interfaces:interface']
    print("\nBelow is the interface details :\n")
    print(f"Name : {int_config['name']}")
    if 'description' in int_config.keys():
        print(f"Description : {int_config['description']}")
    print(f"Type : {int_config['type']}")
    if 'address' in int_config['ietf-ip:ipv4'].keys():
        for i in range(0, len(int_config['ietf-ip:ipv4']['address'])):
            print(f"IP Address : {int_config['ietf-ip:ipv4']['address'][i]['ip']}")
            print(f"Subnet Mask : {int_config['ietf-ip:ipv4']['address'][i]['netmask']}")
    print(f"MAC Address : {int_state['phys-address']}")
    print(f"Incoming packets : {int_state['statistics']['in-unicast-pkts']}")
    print(f"Outgoing packets : {int_state['statistics']['out-unicast-pkts']}")
    print("------------------------------------------------------------")


def main():
    int_list = []
    print("\nBelow are the interface in the router : \n")
    for interface in get_interface_list():
        print(interface['name'])
        int_list.append(interface['name'])
    interface_name = get_interface_name(int_list)
    get_interface_details(interface_name)


if __name__ == '__main__':
    sys.exit(main())
