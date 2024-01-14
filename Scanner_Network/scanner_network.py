import nmap 

destino = "10.0.0.0-255"
port = '22'

nm = nmap.PortScanner()
nm.scan(hosts=destino, ports=port)
if nm.all_hosts():
    print('Host found')
    for host in nm.all_hosts():
        host_ip = host
        host_state = nm[host_ip].state()
        port_state = nm[host_ip]['tcp'][int(port)]['state']
        print(f'{host_ip} - {host_state} - {host_state}')
    else:
            print ('Host not found')
