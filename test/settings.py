import socket
import  platform

DBTYPE = ['Base2_digue', 'Base2_assainissement', 'Base2_eaupotable', 'Base2_eclairagepublic',
         'Base2_chantier', 'Base2_tramway']
CRS = 2154
PGuser = 'pvr'
PGpassword = 'pvr'
PGbase = 'lamiaunittest'

if platform.system() == 'Windows':
    PGhost = 'localhost'
elif platform.system() == 'Linux':
    try:    #docker env in win host
        socket.gethostbyname('docker.for.win.localhost')
        PGhost = 'docker.for.win.localhost'
    except socket.error as e:   # else
        PGhost = 'localhost'

PGport = 5432