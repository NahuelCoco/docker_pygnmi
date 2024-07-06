# Modules
import yaml
from pygnmi.client import gNMIclient

# Variables
host = ('172.20.20.2', '57400')

# Body
if __name__ == '__main__':
    with gNMIclient(target=host, username='admin', password='NokiaSrl1!', insecure=True) as gc:
         result = gc.capabilities() #gc.get(path=['interface[name=ethernet-1/1]'])

    yaml_str = yaml.dump(result, default_flow_style=False)
    print(yaml_str)
#    print("NASHWEEEEEEEEEEEEEEEEEEEEEEEEE")
