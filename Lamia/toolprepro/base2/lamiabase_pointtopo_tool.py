# -*- coding: utf-8 -*-

from qgis.PyQt import uic, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget)
#from ...toolabstract.InspectionDigue_abstract_tool import AbstractInspectionDigueTool
from ...toolabstract.Lamia_abstract_tool import AbstractLamiaTool
import os
import qgis





class BasePointtopoTool(AbstractLamiaTool):

    LOADFIRST = False
    dbasetablename = 'Pointtopo'
    specialfieldui = []

    def __init__(self, dbase, dialog=None, linkedtreewidget=None, gpsutil=None,parentwidget=None, parent=None):
        super(BasePointtopoTool, self).__init__(dbase, dialog, linkedtreewidget,gpsutil, parentwidget, parent=parent)

    def initTool(self):
        # ****************************************************************************************
        # Main spec
        self.CAT = 'Ressources'
        self.NAME = 'Points topo'
        self.dbasetablename = 'Pointtopo'
        self.visualmode = [1,2]        # important : must be child of topographie class, do not use elsewhere
        self.PointENABLED = True
        # self.LineENABLED = True
        # self.PolygonENABLED = True

        self.linkagespec = {'Topographie' :{'tabletc' : None,
                                              'idsource' : 'lpk_topographie',
                                            'idtcsource' : None,
                                           'iddest' : 'pk_topographie',
                                           'idtcdest' : None,
                                           'desttable' : ['Topographie']} }

        self.magicfunctionENABLED = True

        # ****************************************************************************************
        #properties ui
        pass

    def initFieldUI(self):
        # ****************************************************************************************
        #   userui Field
        if self.userwdgfield is None:
            # ****************************************************************************************
            # userui
            self.userwdgfield = UserUI()
            """
            self.linkuserwdg = {'Pointtopo' : {'linkfield' : 'id_pointtopo',
                                             'widgets' : {'typepointtopo': self.userwdg.comboBox_position,
                                                            'x': self.userwdg.doubleSpinBox_X,
                                                            'y': self.userwdg.doubleSpinBox_Y,
                                                            'zmngf': self.userwdg.doubleSpinBox_Zngf,
                                                            'dx': self.userwdg.doubleSpinBox_dX,
                                                            'dy': self.userwdg.doubleSpinBox_dY,
                                                            'dz': self.userwdg.doubleSpinBox_dZ,
                                                            'zwgs84': self.userwdg.doubleSpinBox_Zwgs84,
                                                            'zgps': self.userwdg.doubleSpinBox_Zgps,
                                                            'raf09': self.userwdg.doubleSpinBox_raf09,
                                                            'hauteurperche': self.userwdg.doubleSpinBox_hautperche}},
                                'Topographie': {'linkfield': 'id_topographie',
                                              'widgets': {}}
                                                          }
            """

            self.linkuserwdgfield = {'Pointtopo' : {'linkfield' : 'id_pointtopo',
                                             'widgets' : {'typepointtopo': self.userwdgfield.comboBox_position,
                                                            'x': self.userwdgfield.doubleSpinBox_X,
                                                            'y': self.userwdgfield.doubleSpinBox_Y,
                                                            'zmngf': self.userwdgfield.doubleSpinBox_Zngf,
                                                            'dx': self.userwdgfield.doubleSpinBox_dX,
                                                            'dy': self.userwdgfield.doubleSpinBox_dY,
                                                            'dz': self.userwdgfield.doubleSpinBox_dZ,
                                                            'zwgs84': self.userwdgfield.doubleSpinBox_Zwgs84,
                                                            'zgps': self.userwdgfield.doubleSpinBox_Zgps,
                                                            'raf09': self.userwdgfield.doubleSpinBox_raf09,
                                                            'hauteurperche': self.userwdgfield.doubleSpinBox_hautperche}}
                                                          }
            if self.parentWidget is not None and self.parentWidget.dbasetablename == 'Topographie':
                self.pushButton_addFeature.setEnabled(True)
            else:
                self.pushButton_addFeature.setEnabled(False)

            self.userwdgfield.pushButton_catchvalues.clicked.connect(self.getGPSValues)

            self.gpswidget = {'x' : {'widget' : self.userwdgfield.label_X,
                                     'gga' : 'Xcrs'},
                              'y': {'widget': self.userwdgfield.label_Y,
                                    'gga': 'Ycrs'},
                              'zmngf': {'widget': self.userwdgfield.label_Z,
                                    'gga': 'zmNGF'},
                              'dx': {'widget': self.userwdgfield.label_dX,
                                    'gst': 'xprecision'},
                              'dy': {'widget': self.userwdgfield.label_dY,
                                    'gst': 'yprecision'},
                              'dz': {'widget': self.userwdgfield.label_dZ,
                                    'gst': 'zprecision'},
                              'zgps': {'widget': self.userwdgfield.label_zgps,
                                     'gga': 'elevation'},
                              'zwgs84': {'widget': self.userwdgfield.label_zwgs84,
                                       'gga': 'deltageoid'},
                              'raf09': {'widget': self.userwdgfield.label_raf09,
                                       'gga': 'RAF09'},
                              'hauteurperche': {'widget': self.userwdgfield.label_hautperche,
                                        'gga': 'hauteurperche'}
                              }


    def postloadIds(self,sqlin):
        sqlin += " ORDER BY id_pointtopo "
        if False:
            # sqlin=''
            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                sqlin = "SELECT id_pointtopo FROM Pointtopo_qgis WHERE lpk_topographie = " + str(self.parentWidget.currentFeaturePK)
                sqlin += " ORDER BY id_pointtopo "
            else:
                sqlin += " ORDER BY id_pointtopo "


        return sqlin


    """
    def getPkFromId(self, layername, inputid):
        return inputid





        if False:
            pk = None

            if self.parentWidget is not None and self.parentWidget.currentFeaturePK is not None:
                sql = "SELECT pk_pointtopo FROM Pointtopo_qgis "
                sql += "WHERE id_pointtopo = " + str(inputid)
                sql += " AND lpk_topographie = " + str(self.parentWidget.currentFeaturePK)
                #sql += self.dbase.dateVersionConstraintSQL()
                pk = self.dbase.query(sql)[0][0]

            return pk

    """

    def postOnActivation(self):
        pass

    def postOnDesactivation(self):
        pass


    def postInitFeatureProperties(self, feat):

        if self.currentFeaturePK is None:
            #self.pushButton_savefeature.setEnabled(True)
            self.enablePropertiesButtons(True)
        else:
            # getlpkrevisionbeginfromparent
            sql = "SELECT lpk_revision_begin FROM Pointtopo_qgis WHERE pk_pointtopo = " + str(self.currentFeaturePK)
            result = self.dbase.query(sql)
            if len(result)>0:
                revbegin = result[0][0]
                if revbegin == self.dbase.maxrevision:
                    self.enablePropertiesButtons(True)
                else:
                    self.enablePropertiesButtons(False)
            else:
                self.enablePropertiesButtons(True)

    def enablePropertiesButtons(self, boolvalue):
        self.pushButton_savefeature.setEnabled(boolvalue)
        self.pushButton_addFeature.setEnabled(boolvalue)
        self.pushButton_delFeature.setEnabled(boolvalue)
        self.pushButton_savefeature.setEnabled(boolvalue)
        self.groupBox_geom.setEnabled(boolvalue)


    def magicFunction(self):
        self.featureSelected()
        self.userwdg.comboBox_position.setCurrentIndex(self.userwdg.comboBox_position.findText('Crete'))
        success = self.getGPSValues()
        if success:
            self.saveFeature()


    def createParentFeature(self):

        if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
            if self.parentWidget.dbasetablename == 'Topographie':
                pktopo = self.parentWidget.currentFeaturePK
                pkpointtopo = self.currentFeaturePK
                """
                #idpointtopo
                sql = "SELECT MAX(id_pointtopo) FROM Pointtopo"
                sql += " WHERE lpk_topographie = " + str(pktopo)
                idpointtopo = self.dbase.query(sql)[0][0]
                if idpointtopo is None:
                    idpointtopo = 1
                else:
                    idpointtopo = idpointtopo + 1
                """
                sql = "UPDATE Pointtopo SET "
                sql += "lpk_topographie = " + str(pktopo)
                sql += ", id_pointtopo = " + str(pkpointtopo)
                sql += " WHERE pk_pointtopo = " + str(pkpointtopo) + ";"
                query = self.dbase.query(sql)
                self.dbase.commit()


        if False:

            pktopo = self.currentFeature.id()
            lastobjetid = self.dbase.getLastId('Pointtopo') + 1
            lastrevision = self.dbase.getLastPk('Revision')

            sql = "UPDATE Pointtopo SET "
            sql += "id_pointtopo = " + str(lastobjetid)   + ","
            sql += "id_revisionbegin = " + str(lastrevision)
            sql += " WHERE pk_pointtopo = " + str(pktopo) + ";"
            query = self.dbase.query(sql)
            self.dbase.commit()



            #print('parent',pktopo)
            if self.parentWidget is not None and self.parentWidget.currentFeature is not None:
                if self.parentWidget.dbasetablename == 'Topographie':
                    # print('parent levetopo')
                    currentparentlinkfield = self.parentWidget.currentFeature['id_topographie']
                    sql = "UPDATE Pointtopo SET id_topographie = " + str(currentparentlinkfield) + " WHERE pk_pointtopo = " + str(pktopo) + ";"
                    self.dbase.query(sql)
                    self.dbase.commit()



    def deleteParentFeature(self):
        return True


    def postSaveFeature(self, boolnewfeature):
        pass


    def getGPSValues(self):
        if self.gpsutil is not None:
            if self.gpsutil.currentpoint is None:
                self.windowdialog.errorMessage('GPS non connecte')
                return

            for i, fieldname in enumerate(self.gpswidget.keys()):
                try:
                    value = float(self.gpswidget[fieldname]['widget'].text())
                except ValueError:
                    value = None
                if value is not None:
                    self.linkuserwdg[self.dbasetablename]['widgets'][fieldname].setValue(value)
                else:
                    self.linkuserwdg[self.dbasetablename]['widgets'][fieldname].setValue(-1.0)
            if False:
                if self.rubberBand is not None:
                    self.rubberBand.reset(0)
                else:
                    self.rubberBand = qgis.gui.QgsRubberBand(self.canvas,0)
                    self.rubberBand.setWidth(5)
                    self.rubberBand.setColor(QtGui.QColor("magenta"))
            self.createorresetRubberband(0)
            self.setTempGeometry([self.gpsutil.currentpoint],False)
            return True
        else:
            self.errorMessage('GPS non connecte')
            return False




class UserUI(QWidget):
    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), 'lamiabase_pointtopo_tool_ui.ui')
        uic.loadUi(uipath, self)