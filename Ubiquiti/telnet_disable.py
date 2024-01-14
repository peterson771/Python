from netmiko import ConnectHandler

# Define as credenciais de acesso ao equipamento
device = {
    'device_type': 'ubiquiti_edgerouter',
    'ip': '10.0.10.7',
    'port': 2222,
    'username': 'viavelozredes',
    'password': 'v2rf!bR@'
}

# Cria uma conexão SSH com o equipamento
ssh = ConnectHandler(**device)

# Executa um comando remoto
output = ssh.send_command('ls')

# Exibe a saída do comando no console
print(output)

# Encerra a conexão
ssh.disconnect()