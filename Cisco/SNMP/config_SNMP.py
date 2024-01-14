from netmiko import ConnectHandler

cisco_nexus_R1 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'admin',
    'password': 'secret1234',
    'port' : 22,
    }

cisco_nexus_R2 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.20',
    'username': 'admin',
    'password': 'secret1234',
    'port' : 22,
    }
    
cisco_nexus_R3  = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.30',
    'username': 'admin',
    'password': 'secret1234',
    'port' : 22,
    }
    
cisco_nexus_R4 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.40',
    'username': 'admin',
    'password': 'secret1234',
    'port' : 22,
    }
	
with open ('SNMP.txt') as f:
	lines = f.read().splitlines()
print (lines)
    
all_devices = [cisco_nexus_R1, cisco_nexus_R2, cisco_nexus_R3, cisco_nexus_R4]
    
for devices in all_devices:    
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set (lines)
    print (output)
        