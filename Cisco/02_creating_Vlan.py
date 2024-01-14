################################################
############### Unico Switch ###################
################################################


from netmiko import ConnectHandler

cisco_nexus_R1 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'admin',
    'password': 'secret1234',
    'port' : 22,
    }
	
net_connect = ConnectHandler(**cisco_nexus_R1)
output = net_connect.send_command('show ip int brief')
print = (output)

for n in range (90,100):
	print (" Creating Vlan " + str(n))
	config_commands = ['vlan ' + str(n), 'name Pyhton_VLAN ' + str(n)]
	output = net_connect.send_config_set(config_commands)
	print (output)
	
#################################################### 
############### Mutiplos Switchs ###################
####################################################

    
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
    
all_devices = [cisco_nexus_R1, cisco_nexus_R2, cisco_nexus_R3, cisco_nexus_R4]
    
for devices in all_devices:    
    connect = ConnectHandler(**devices)
    for n in range (12, 18):
        print (" Creating Vlan " + str(n))
        config_commands = ['vlan ' + str(n), 'name Pyhton_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output)
    
 
