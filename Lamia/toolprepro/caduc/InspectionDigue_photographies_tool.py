# -*- coding: utf-8 -*-

"""
/***************************************************************************
 PostTelemac
                                 A QGIS plugin
 Post Traitment or Telemac
                              -------------------
        begin                : 2015-07-07
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Artelia
        email                : patrice.Verchere@arteliagroup.com
 ***************************************************************************/
 
 ***************************************************************************/
 get Image class
 Generate a Qimage from selafin file to be displayed in map canvas 
 with tht draw method of posttelemacpluginlayer
 
Versions :
0.0 : debut

 ***************************************************************************/
"""


from qgis.PyQt import uic, QtCore, QtGui
from .InspectionDigue_abstract_tool import AbstractInspectionDigueTool
import qgis
import os
import glob
import datetime

from ..maptool.mapTools import mapToolAddFeature, mapToolAddLine, mapToolCapture


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'photographiesTool.ui'))



class photographiesTool(AbstractInspectionDigueTool,FORM_CLASS):

    def __init__(self, dbase,dialog, linkedtreewidget, parent=None):
        super(photographiesTool,self).__init__(dbase,dialog,linkedtreewidget,parent = parent)

        
    def initTool(self):
        self.setupUi(self)
        self.CAT = 'Photographies'
        self.NAME = 'Photographies'
        self.sourcelayername = 'photographies'
        #self.iconpath = os.path.join(os.path.dirname(__file__),'..','icons','tools','Video_48x48.png' )
        self.pickoptions = [[self.pushButton_Pick_view,self.pushButton_show_link,self.comboBox_link_des, self.spinBox__link_des_id]]
        self.pushButton_chooseph.clicked.connect(self.choosePhoto)
        self.pushButton_lastph.clicked.connect(self.lastPhoto)
        
    def onActivation(self):
        pass


    def onDesactivation(self):
        pass


        
    def showFeatureWidget(self,featureid = None):
        if self.lineEdit_ph_file.text() != '':
            self.showPhoto()
        else:
            self.label_photo.setText('/')
            
    def choosePhoto(self):
        file, extension = self.windowdialog.qfiledlg.getOpenFileNameAndFilter(None, 'Choose the file', self.windowdialog.imagedir,
                                                                 'Image (*.jpg)', '')
        if file:
            self.lineEdit_ph_file.setText(os.path.normpath(file))
            
            import PIL.Image
            img = PIL.Image.open(os.path.normpath(file))
            #exif_data = img._getexif()
            #print(img._getexif())
            import PIL.ExifTags
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

            try:
                temp = exif['GPSInfo'][2]
                #print(exif)
                #print(temp[0][0] ,temp[1][0] ,temp[2][0])
                latsecond = float( str(temp[2][0])[0:2] + '.' + str(temp[2][0])[2:-1] )/3600.0
                #print(temp[0][0] ,temp[1][0] ,latsecond)
                lat = temp[0][0] + temp[1][0]/60.0 + latsecond
                
                
                temp = exif['GPSInfo'][4]
                #print(temp[0][0] ,temp[1][0] ,temp[2][0])
                longsecond = float( str(temp[2][0])[0:2] + '.' + str(temp[2][0])[2:-1] )/3600.0
                long = temp[0][0] + temp[1][0]/60.0 + longsecond
                if exif['GPSInfo'][3] != 'E':
                    long = -long
                #print(long, lat)
                #crsSrc = qgis.core.QgsCoordinateReferenceSystem(4326,  qgis.core.QgsCoordinateReferenceSystem.PostgisCrsId)
                crsSrc = qgis.core.QgsCoordinateReferenceSystem(4326)
                destcrs = self.canvas.mapSettings().destinationCrs()
                #destcrs = self.layers[0].crs()
                xform = qgis.core.QgsCoordinateTransform(crsSrc, destcrs )
                pt1 = xform.transform(qgis.core.QgsPoint(long,lat))
                #print(pt1)
                self.actuallayerindex = 0
                self.setTempGeometry([pt1])
            except KeyError as e:
                pass
            
            self.showPhoto()
        
    def lastPhoto(self):
        list_of_files = glob.glob(self.windowdialog.imagedir+"\*.jpg")
        #print([datetime.datetime.fromtimestamp(os.path.getctime(file)).strftime('%Y-%m-%d %H:%M:%S') for file in list_of_files])
        latest_file = max(list_of_files, key=os.path.getctime)
        self.lineEdit_ph_file.setText(os.path.normpath(latest_file))
        self.showPhoto()
        
    def showPhoto(self):

        if  self.lineEdit_ph_file.text()[0] == '.':
            filetoeval = '"' + os.path.dirname(self.dbase.dbasefile) + '","' + '","'.join(self.lineEdit_ph_file.text().split('\\')) + '"'
            #filetoeval = '"' + os.path.normpath(os.path.dirname(self.dbase.dbasefile)) + '","' + '","'.join(self.lineEdit_ph_file.text().split('\\')) + '"'
            #print(filetoeval)

            file = eval("os.path.join(" + filetoeval + ")")

            #print('file',file)

        else :
            file = os.path.normpath(self.lineEdit_ph_file.text())


        if os.path.isfile(file):
            self.label_photo.clear()
            myPixmap = QtGui.QPixmap(file)
            myScaledPixmapH = myPixmap.scaledToHeight(self.label_photo.size().height())
            myScaledPixmapW = myPixmap.scaledToWidth(self.label_photo.size().width())
            if myScaledPixmapH.size().height() < myScaledPixmapW.size().height():
                self.label_photo.setPixmap(myScaledPixmapH)
            else:
                self.label_photo.setPixmap(myScaledPixmapW)
        else:
            self.label_photo.setText('photo non trouvee')
        
        
        
        

        
        
        
        

        
