import socket
import ipaddress
try:
    # socket.inet_aton('localhost')
    # ipaddress.ip_address('docker.for.win.localhost')
    print(socket.gethostbyname('docker.for.win.localhost:5432'))
    print('ok')
except socket.error as e:
    # Not legal
    print('nok',e)