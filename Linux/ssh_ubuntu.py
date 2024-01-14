from netmiko import ConnectHandler

# Define os dados de conexão com o servidor Ubuntu
device = {
    'device_type': 'linux',
    'ip': '10.0.21.81',
    'username': 'peterson',
    'password': 'Paty2608',
}

# Cria uma sessão SSH com o servidor Ubuntu
with ConnectHandler(**device) as ssh:
    # Executa o comando sudo apt install net-tools
    output = ssh.send_command('sudo apt update && sudo apt install -y net-tools', expect_string=r'\[sudo\] password')
    output += ssh.send_command('Paty2608', expect_string=r'\$')
    print(output)
