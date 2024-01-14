from sys import stderr, stdin, stdout
import paramiko

address = '10.0.0.10'
username = 'root'
password = 'olaolaola'

ssh = paramiko.SSHClient()
ssh.net_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('ifconfig')
stdin.close()
for line in stdout.readline():
    print (line.split('\n'))