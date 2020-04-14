import socket

DBTYPE = ['Base2_digue', 'Base2_assainissement', 'Base2_eaupotable', 'Base2_eclairagepublic']
CRS = 2154
PGuser = 'pvr'
PGpassword = 'pvr'
PGbase = 'Lamiaunittest'
try:    #docker env in win host
    socket.gethostbyname('docker.for.win.localhost')
    PGhost = 'docker.for.win.localhost'
except socket.error as e:   # else
    PGhost = 'localhost'

PGport = 5432