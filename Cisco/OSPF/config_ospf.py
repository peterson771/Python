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
    
cisco_nexus_R4 = {
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

for routers in (cisco_nexus_R2, cisco_nexus_R2, cisco_nexus_R2, cisco_nexus_R2)
    connect = ConnectHandler(**routers)
    print(connect.find_prompt())
    output = connect.send_config_from_file('config_ospf.txt')
    print(output)
    