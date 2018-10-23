# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GPS2PointDockWidget
                                 A QGIS plugin
 gps to point
                             -------------------
        begin                : 2017-06-16
        git sha              : $Format:%H$
        copyright            : (C) 2017 by ARTELIA
        email                : aa
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import qgis
import sys
import qgis.utils
qgis.utils.uninstallErrorHook()     #for standart output

#import serial
import time
import threading

from qgis.PyQt import QtGui, uic, QtCore
from qgis.PyQt.QtCore import pyqtSignal



class GpsUtil(QtCore.QObject):
    qgssentence = QtCore.pyqtSignal(dict)
    ggasentence = QtCore.pyqtSignal(dict)
    gstsentence = QtCore.pyqtSignal(dict)
    GPSConnected = pyqtSignal(bool)

    def __init__(self):
        """Constructor."""
        super(QtCore.QObject,self).__init__()
        
        self.connection = None
        self.crs = None
        self.wgs84CRS = qgis.core.QgsCoordinateReferenceSystem(4326)
        self.xform = None
        self.currentpoint = None

        self.receiveGPGGA = False
        self.receiveGPGST = False

        self.hauteurperche = 0.0

        try:
            self.qgisversion_int = qgis.utils.QGis.QGIS_VERSION_INT
        except AttributeError:  #qgis 3
            self.qgisversion_int = qgis.utils.Qgis.QGIS_VERSION_INT

        #raf09
        self.raf09filepath = os.path.join(os.path.dirname(__file__),'raf09.mnt')
        if sys.version_info.major == 2:
            self.raf09file = open(self.raf09filepath,'r')
        elif sys.version_info.major == 3:
            self.raf09file = open(self.raf09filepath, 'r')

        line1 = self.raf09file.readline().strip()
        linelist = line1.split(' ')
        self.minlong = float(linelist[0])
        self.maxlong = float(linelist[1])
        self.minlat = float(linelist[2])
        self.maxlat = float(linelist[3])
        self.paslong = float(linelist[4])
        self.paslat = float(linelist[5])

        self.lenx = int((self.maxlong - self.minlong) / self.paslong) + 1
        #self.leny = int((self.maxlat - self.minlat) / self.paslat)
        self.lenline1 = len(line1) + 2
        self.raf09file.close()

        


    def setCRS(self,crs):
        self.crs = crs
        if int(str(self.qgisversion_int)[0:3]) < 220:
            self.xform = qgis.core.QgsCoordinateTransform(self.wgs84CRS,
                                                          self.crs)
        else:
            self.xform = qgis.core.QgsCoordinateTransform(self.wgs84CRS,
                                                          self.crs,
                                                          qgis.core.QgsProject.instance())



    def connectionLost(self):
        print('connectionLost')
        try:
            self.connection.nmeaSentenceReceived.disconnect(self.collectNMEA)
            self.connection.stateChanged.disconnect(self.gpsStateChanged)
        except:
            pass

        self.receiveGPGGA = False
        self.receiveGPGST = False

        self.currentpoint = None
        self.GPSConnected.emit(False)

    def connectToGPS(self):

            try:
                self.connection.nmeaSentenceReceived.disconnect(self.collectNMEA)
            except Exception as e:
                pass

            if int(qgis.PyQt.QtCore.QT_VERSION_STR[0]) == 4:
                connectionRegistry = qgis.core.QgsGPSConnectionRegistry().instance()
            elif int(qgis.PyQt.QtCore.QT_VERSION_STR[0]) == 5:  # qgis3
                connectionRegistry = qgis.core.QgsApplication.gpsConnectionRegistry()

            connectionList = connectionRegistry.connectionList()
            if len(connectionList) > 0 and connectionList[0] is not None:
                self.connection = connectionList[0]
                # print('connected')
                self.receiveGPGGA = False
                self.receiveGPGST = False
                self.connection.nmeaSentenceReceived.connect(self.collectNMEA)
                #self.connection.stateChanged.connect(self.gpsStateChanged)
                self.connection.destroyed.connect(self.connectionLost)
                self.GPSConnected.emit(True)
                #self.raf09file = open(self.raf09filepath ,'r')
                if sys.version_info.major == 2:
                    self.raf09file = open(self.raf09filepath, 'r')
                elif sys.version_info.major == 3:
                    self.raf09file = open(self.raf09filepath, 'rb')
            else:
                self.errorMessage('Connecter d abord le GPS de QGIS')

    """
    def gpsStateChanged(self, gpsInfo):

        if gpsInfo.status != 3:
            try:
                self.connection.nmeaSentenceReceived.disconnect(self.collectNMEA)
                self.connection.stateChanged.disconnect(self.gpsStateChanged)
            except:
                pass
            self.GPSConnected.emit(False)
    """

    def closeConnection(self):
        try:
            self.connection.nmeaSentenceReceived.disconnect(self.collectNMEA)
        except:
            pass
        try:
            self.connection.stateChanged.disconnect(self.gpsStateChanged)
        except:
            pass
        self.connection = None
        self.raf09file.close()
        self.GPSConnected.emit(False)


    def collectNMEA(self, sentence):

        if not self.receiveGPGGA:
            self.ggasentence.emit(self.getQgsResult())

        if sentence.split(',')[0] == '$GPGGA':
            self.receiveGPGGA = True
            #self.lineEdit_gga.setText(sentence)
            resultGGA = self.getGPGGAResult(sentence.split(','))
            #self.label_Z.setText(str(round(self.resultGGA['elevation'], 2)))
            self.ggasentence.emit(resultGGA)

        if sentence.split(',')[0] == '$GPGST':
            self.receiveGPGST = True
            #self.lineEdit_gst.setText(sentence)
            resultGST = self.getGPGSTResult(sentence.split(','))
            #self.label_XP.setText(str(round(self.resultGST['xprecision'], 2)))
            #self.label_YP.setText(str(round(self.resultGST['yprecision'], 2)))
            #self.label_ZP.setText(str(round(self.resultGST['zprecision'], 2)))
            self.gstsentence.emit(resultGST)

    def getQgsResult(self):
        try:
            result = {}
            result['sentence'] = None
            result['latitude'] = self.connection.currentGPSInformation().latitude
            result['longitude'] = self.connection.currentGPSInformation().longitude
            result['quality'] = self.connection.currentGPSInformation().quality

            result['elevation'] = None
            result['deltageoid'] = None
            zconvert = None
            result['RAF09'] = None
            result['zmNGF'] = None
            result['hauteurperche'] = self.hauteurperche

            if int(str(self.qgisversion_int)[0:3]) < 220:
                wgs84point = qgis.core.QgsPoint(result['longitude'], result['latitude'])
            else:
                wgs84point = qgis.core.QgsPointXY(result['longitude'], result['latitude'])

            if self.xform is not None:
                crspoint = self.xform.transform(wgs84point)
                result['Xcrs'] = crspoint.x()
                result['Ycrs'] = crspoint.y()
                result['QgsPoint'] = crspoint
                self.currentpoint = crspoint
            else:
                result['Xcrs'] = 0.0
                result['Ycrs'] = 0.0
                result['QgsPoint'] = None
                #self.currentpoint = crspoint

            return result
        except Exception as e:
            print('error nmeaGGA', e)
            result = {}
            return result

    def getGPGGAResult(self, sentence):
        try:
            result = {}
            result['sentence'] = sentence
            result['latitude'] = float(sentence[2][0:2]) + float(sentence[2][2:11]) / 60
            if sentence[3] == 'S':
                result['latitude'] = - result['latitude']
            result['longitude'] = float(sentence[4][0:3]) + float(
                sentence[4][3:11]) / 60  # + float(data[4][6:11])/3600.0
            if sentence[5] == 'W':
                result['longitude'] = - result['longitude']
            result['quality'] = sentence[6]

            result['elevation'] = float(sentence[9]) - self.hauteurperche
            result['deltageoid'] = float(sentence[11])
            result['hauteurperche'] = self.hauteurperche
            zconvert = self.getRAF09ZConvert(result['longitude'],result['latitude'] )
            result['RAF09'] = zconvert
            result['zmNGF'] = result['elevation'] + result['deltageoid'] - zconvert

            if int(str(self.qgisversion_int)[0:3]) < 220:
                wgs84point = qgis.core.QgsPoint(result['longitude'], result['latitude'])
            else:
                wgs84point = qgis.core.QgsPointXY(result['longitude'], result['latitude'])
            if self.xform is not None:
                crspoint = self.xform.transform(wgs84point)
                result['Xcrs'] = crspoint.x()
                result['Ycrs'] = crspoint.y()
                result['QgsPoint'] = crspoint
                self.currentpoint = crspoint
            else:
                result['Xcrs'] = 0.0
                result['Ycrs'] = 0.0
                result['QgsPoint'] = None
                #self.currentpoint = crspoint


            return result
        except Exception as e:
            print('error nmeaGGA', e)
            result = {}
            return result

    def getGPGSTResult(self, sentence):
        try:
            result = {}
            result['sentence'] = sentence
            result['xprecision'] = float(sentence[6])
            result['yprecision'] = float(sentence[7])
            result['zprecision'] = float(sentence[8].split('*')[0])
            return result
        except Exception as e:
            print('error nmeaGST', e)
            result = {}
            return result


    def getRAF09ZConvert(self,x,y):

        #point1 - x1 y1

        # print(self.minlong,self.paslong, self.maxlat,self.paslat )

        xindex = abs(int((x - self.minlong) / self.paslong))
        yindex = abs(int((y - self.maxlat) / self.paslat))
        seekindex = self.lenline1 + (yindex * self.lenx + xindex) * 10

        # print('seekindex',seekindex)

        self.raf09file.seek(seekindex)
        # print('okokok', self.raf09file.read(7))
        raf1 = float(self.raf09file.read(7))
        raf1x = (self.minlong + xindex * self.paslong)
        raf1y = (self.maxlat - yindex * self.paslat)

        # print('raf1', raf1,raf1x, raf1y )

        #point2 (x suivant) - x2 y1
        self.raf09file.seek(3,1)
        raf2 = float(self.raf09file.read(7))
        #point3             x1 y2
        self.raf09file.seek(3 + self.lenx*10 - 20 ,1)
        raf3 = float(self.raf09file.read(7))
        #point4             x2 y2
        self.raf09file.seek(3,1)
        raf4 = float(self.raf09file.read(7))

        #resolution bilineaire
        Dfx = raf2 - raf1
        Dfy = raf3 - raf1
        Dfxy = raf1 + raf4 - raf3 - raf2
        dx = x - raf1x
        dy = -(y - raf1y)
        Dx = self.paslong
        Dy = self.paslat

        raf09convert = Dfx*dx/Dx + Dfy*dy/Dy + Dfxy*dx*dy/Dx/Dy + raf1

        return raf09convert






            
    def errorMessage(self,text):

        if qgis.utils.iface is not None:
            if int(str(self.qgisversion_int)[0:3]) < 220:
                qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.gui.QgsMessageBar.CRITICAL, duration=3)
            else:
                qgis.utils.iface.messageBar().pushMessage("InspectionDigue", text,
                                                      level=qgis.core.Qgis.Warning, duration=3)
        else:
            print('ErrorMessage', text)