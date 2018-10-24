# -*- coding: utf-8 -*-

import os
import numpy as np

raffile = os.path.join(os.path.dirname(__file__),'..','gps','raf09.mnt')

f = open(raffile, 'r')
line1 = f.readline().strip()

print(line1,len(line1))

linelist = line1.split(' ')
minlong = float(linelist[0])
maxlong = float(linelist[1])
minlat = float(linelist[2])
maxlat = float(linelist[3])
paslong = float(linelist[4])
paslat = float(linelist[5])

lenline1 = len(line1)+2

lenx = int((maxlong - minlong)/paslong) +1
leny = int((maxlat - minlat)/paslat)

print('lenx y',lenx,leny )

if False:
    #test valeur 0

    f.seek(longline1)
    print('test value 0 ',f.read(7))

#test seek
if False:


    if True:
        xindex = 1
        yindex = 2

    print(xindex, yindex)
    #seekindex = longline1 + (yindex * leny + xindex)*11
    seekindex = longline1 + (yindex * lenx + xindex)*10

    f.seek(seekindex)
    print('resulttestsek',f.read(7))

if False:
    #tets valeur reelle

    x = -5.44390
    y = 51.41373

    xindex = abs(int((x - minlong)/paslong))
    yindex = abs(int((y - maxlat)/paslat))

    print('index',xindex,yindex)

    seekindex = longline1 + (yindex * lenx + xindex)*10

    f.seek(seekindex)
    print('resultpoint',f.read(7))

if True:
    x = -0.71474
    y = 44.86133

    if True:
        xindex = abs(int((x - minlong)/paslong))
        yindex = abs(int((y - maxlat)/paslat))

    print('index',xindex,yindex)

    seekindex = lenline1 + (yindex * lenx + xindex)*10

    f.seek(seekindex)
    print('resultpoint',f.read(7))

    f.seek(3,1)
    print('resultpoint2', f.read(7))

    f.seek(3 + lenx*10 - 20 ,1)
    print('resultpoint3', f.read(7))

    f.seek(3,1)
    print('resultpoint4', f.read(7))


if True:
    #point1 - x1 y1

    x = -0.71569
    y = 44.86273

    xindex = abs(int((x - minlong) / paslong))
    yindex = abs(int((y - maxlat) / paslat))
    seekindex = lenline1 + (yindex * lenx + xindex) * 10
    f.seek(seekindex)
    raf1 = float(f.read(7))
    raf1x = (minlong + xindex*paslong)
    raf1y =  (maxlat - yindex*paslat)

    print('raf1xy', raf1x, raf1y)

    #point2 (x suivant) - x2 y1
    f.seek(3,1)
    raf2 = float(f.read(7))
    #point3             x1 y2
    f.seek(3 + lenx*10 - 20 ,1)
    raf3 = float(f.read(7))
    #point4             x2 y2
    f.seek(3,1)
    raf4 = float(f.read(7))

    print('raf', raf1, raf2, raf3, raf4)

    #resolution bilineaire
    Dfx = raf2 - raf1
    Dfy = raf3 - raf1
    Dfxy = raf1 + raf4 - raf3 - raf2
    dx = x - raf1x
    dy = -(y - raf1y)
    Dx = paslong
    Dy = paslat

    print('d', Dfx, Dfy, Dfxy, dx,dy,Dx,Dy  )

    rafpoint = Dfx*dx/Dx + Dfy*dy/Dy + Dfxy*dx*dy/Dx/Dy + raf1

    print('result',rafpoint)


f.close()

