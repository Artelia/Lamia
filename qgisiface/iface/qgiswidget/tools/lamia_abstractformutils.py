# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This file is part of LAMIA.

    LAMIA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    LAMIA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
"""
  * Copyright (c) 2017-2020 ARTELIA Commit <lamia@arteliagroup.com>
  * 
  * SPDX-License-Identifier: GPL-3.0-or-later
  * License-Filename: LICENSING.md
"""
"""
from qgis.PyQt.QtWidgets import (QWidget, QTreeWidgetItem, QMessageBox, QFileDialog, QTableWidget,
                                     QHeaderView, QComboBox, QSpinBox,QCheckBox, QPushButton, QDateEdit,QDateTimeEdit, QTextEdit,
                                     QDoubleSpinBox, QDialog, QVBoxLayout, QTreeWidget, QLineEdit, QCheckBox,
                                     QLabel, QMessageBox, QTextBrowser, QTableWidgetItem,QApplication,QToolButton, QAbstractItemView,
                                     QTabWidget)
"""
from qgis.PyQt.QtWidgets import (
    QComboBox,
    QTextEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QDateEdit,
    QDateTimeEdit,
    QTextBrowser,
    QCheckBox,
    QLabel,
    QTabWidget,
    QTabBar,
    QStackedWidget,
    QToolButton,
    QPushButton,
)
from qgis.PyQt import QtCore
import qgis, logging, datetime, os
import qgis.core


class FormToolUtils(QtCore.QObject):
    def __init__(self, formtoolwidget):
        super(FormToolUtils, self).__init__()
        self.formtoolwidget = formtoolwidget

    def ____________actionsOnWidgetCreation(self):
        pass

    def initWidgetBehaviour(self):
        templinkuserwgd = self.formtoolwidget.formtoolwidgetconfdict
        if templinkuserwgd is None:
            raise TypeError(
                "formtoolwidgetconfdict of {} is None".format(
                    self.formtoolwidget.DBASETABLENAME
                )
            )

        # set multirowtab
        tabwidgets = self.formtoolwidget.toolwidget.findChildren(QTabWidget)
        # https://forum.qt.io/topic/21391/tab-widget-tab-height-to-accommodate-2-line-tab-names/2
        for tabwdg in tabwidgets:
            tabbar = tabwdg.tabBar()
            for index in range(tabbar.count()):
                text = tabbar.tabText(index)
                if r"\n" in text.strip():
                    txtsplit = text.split(r"\n")
                    newtxt = "\n".join(txtsplit)
                    qlab = QLabel(newtxt, tabwdg)
                    qlab.setTextFormat(QtCore.Qt.PlainText)
                    tabbar.setTabText(index, "")
                    tabwdg.tabBar().setTabButton(index, QTabBar.RightSide, qlab)

        for tablename in templinkuserwgd:
            dbasetables = self.formtoolwidget.dbase.dbasetables

            if tablename in dbasetables.keys():
                dbasetable = dbasetables[tablename]
                for field in dbasetable["fields"].keys():

                    # for linkuserwdg in [self.linkuserwdg]:
                    for linkuserwdg in [templinkuserwgd]:
                        if linkuserwdg is None or linkuserwdg.keys() is None:
                            continue
                        if (
                            tablename in linkuserwdg.keys()
                            and field in linkuserwdg[tablename]["widgets"].keys()
                        ):

                            wdgs = linkuserwdg[tablename]["widgets"][field]
                            if "Cst" in dbasetable["fields"][field].keys():
                                # combox filling with constraints
                                if isinstance(wdgs, QComboBox) or (
                                    isinstance(wdgs, list)
                                    and isinstance(wdgs[0], QComboBox)
                                ):

                                    templist = [
                                        description[0]
                                        for description in dbasetable["fields"][field][
                                            "Cst"
                                        ]
                                    ]

                                    if isinstance(wdgs, QComboBox):
                                        wdgs = [wdgs]
                                    for wdg in wdgs:
                                        wdg.clear()
                                        wdg.addItems(templist)

                            if "ParFldCst" in dbasetable["fields"][field].keys():
                                nameparentfield = dbasetable["fields"][field][
                                    "ParFldCst"
                                ]
                                # userwidget
                                if (
                                    tablename in linkuserwdg.keys()
                                    and "widgets" in linkuserwdg[tablename].keys()
                                    and nameparentfield
                                    in linkuserwdg[tablename]["widgets"].keys()
                                    and isinstance(
                                        linkuserwdg[tablename]["widgets"][
                                            nameparentfield
                                        ],
                                        QComboBox,
                                    )
                                ):
                                    linkuserwdg[tablename]["widgets"][
                                        nameparentfield
                                    ].currentIndexChanged.connect(
                                        self.comboparentValueChanged
                                    )

                            # multiple wdg for field management
                            if isinstance(wdgs, list) and len(wdgs) > 1:
                                if isinstance(wdgs[0], QComboBox):
                                    for wdg in wdgs:
                                        wdg.currentIndexChanged.connect(
                                            self.manageMultipleWidgetField
                                        )
                                elif isinstance(wdgs[0], QSpinBox) or isinstance(
                                    wdgs[0], QDoubleSpinBox
                                ):
                                    for wdg in wdgs:
                                        wdg.valueChanged.connect(
                                            self.manageMultipleWidgetField
                                        )
                                elif isinstance(wdgs[0], QTextBrowser) or isinstance(
                                    wdgs[0], QLineEdit
                                ):
                                    for wdg in wdgs:
                                        wdg.textChanged.connect(
                                            self.manageMultipleWidgetField
                                        )
                                elif isinstance(wdgs[0], QDateEdit) or isinstance(
                                    wdgs[0], QDateTimeEdit
                                ):
                                    for wdg in wdgs:
                                        wdg.dateChanged.connect(
                                            self.manageMultipleWidgetField
                                        )

                            # case TABLEFILTERFIELD : set field unselectionnable
                            if field in self.formtoolwidget.TABLEFILTERFIELD.keys():
                                wdg.setEnabled(False)

                            if not isinstance(wdgs, list):
                                wdgs = [wdgs]
                            for wdg in wdgs:
                                wdg.setToolTip(f"{tablename}.{field}")

    def connectSubWidgetModifications(self):
        for table, tabledict in self.formtoolwidget.formtoolwidgetconfdict.items():
            for field, wdg in tabledict["widgets"].items():
                if isinstance(wdg, QTextEdit) or isinstance(wdg, QLineEdit):
                    wdg.textChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
                    wdg.valueChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QComboBox):
                    wdg.currentIndexChanged.connect(
                        self.formtoolwidget.subwidgetChanged
                    )
                elif isinstance(wdg, QDateEdit):
                    wdg.dateChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QDateTimeEdit):
                    wdg.dateTimeChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QCheckBox):
                    wdg.stateChanged.connect(self.formtoolwidget.subwidgetChanged)
                elif isinstance(wdg, QLabel):
                    pass

    def manageMultipleWidgetField(self):
        """
        Activated by widget.valueChanged or widget.currentIndexChanged signal

        Manage multiple combobox or spinbox linked to one table field
        """
        senderwdg = self.sender()

        for tablename in self.formtoolwidget.formtoolwidgetconfdict:
            for fieldname in self.formtoolwidget.formtoolwidgetconfdict[tablename][
                "widgets"
            ].keys():
                wdgs = self.formtoolwidget.formtoolwidgetconfdict[tablename]["widgets"][
                    fieldname
                ]

                if isinstance(wdgs, list) and senderwdg in wdgs:
                    if isinstance(senderwdg, QComboBox):
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.currentIndexChanged.disconnect(
                                        self.manageMultipleWidgetField
                                    )
                                except:
                                    pass
                                wdg.setCurrentIndex(senderwdg.currentIndex())
                                wdg.currentIndexChanged.connect(
                                    self.manageMultipleWidgetField
                                )
                        break
                    elif isinstance(senderwdg, QSpinBox) or isinstance(
                        senderwdg, QDoubleSpinBox
                    ):
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.valueChanged.disconnect(
                                        self.manageMultipleWidgetField
                                    )
                                except:
                                    pass
                                wdg.setValue(senderwdg.value())
                                wdg.valueChanged.connect(self.manageMultipleWidgetField)
                        break

                    elif isinstance(senderwdg, QTextBrowser) or isinstance(
                        senderwdg, QLineEdit
                    ):

                        texttocopy = ""
                        if isinstance(senderwdg, QTextBrowser):
                            texttocopy = senderwdg.toPlainText()
                        else:
                            texttocopy = senderwdg.text()
                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.textChanged.disconnect(
                                        self.manageMultipleWidgetField
                                    )
                                except:
                                    pass

                                if isinstance(wdg, QTextBrowser):
                                    wdg.setPlainText(texttocopy)
                                else:
                                    wdg.setText(texttocopy)
                                wdg.textChanged.connect(self.manageMultipleWidgetField)
                        break

                    elif isinstance(senderwdg, QDateEdit) or isinstance(
                        senderwdg, QDateTimeEdit
                    ):

                        datetocopy = senderwdg.dateTime()

                        for wdg in wdgs:
                            if wdg != senderwdg:
                                try:
                                    wdg.dateChanged.disconnect(
                                        self.manageMultipleWidgetField
                                    )
                                except:
                                    pass
                                wdg.setDateTime(datetocopy)
                                wdg.dateChanged.connect(self.manageMultipleWidgetField)
                        break

    def comboparentValueChanged(
        self,
        index,
        parenttablename=None,
        parentfieldname=None,
        childfield=None,
        combochild=None,
    ):
        """
        Activated by currentIndexChanged

        Manage paret/child combobox
        specify tablename, parentfield, childfield and combochild for not combo included in formtoolwidgetconfdict
        """

        debug = False
        if debug:
            senderwdg = self.sender()
            print("**", senderwdg.objectName())

        senderwdg = self.sender()
        if (
            isinstance(senderwdg, QComboBox) and senderwdg.count() == 0
        ):  # case triple descendant and parent not filled
            return

        if parenttablename is None and parentfieldname is None:
            if (
                self.formtoolwidget.toolwidget == self.formtoolwidget.toolwidgetmain
                or self.formtoolwidget.toolwidget
                == self.formtoolwidget.toolwidgetadvanced
            ):
                comefromrawtable = False
                if self.formtoolwidget.formtoolwidgetconfdict is not None:
                    for (
                        tablename,
                        tabledict,
                    ) in self.formtoolwidget.formtoolwidgetconfdict.items():
                        for fieldname in tabledict["widgets"].keys():
                            if senderwdg == tabledict["widgets"][fieldname]:
                                parenttablename = tablename
                                parentfieldname = fieldname
                                break
        else:
            comefromrawtable = False

        if parenttablename is None:
            return

        try:
            parentcstvalue = self.formtoolwidget.dbase.getConstraintRawValueFromText(
                parenttablename, parentfieldname, senderwdg.currentText()
            )
        except Exception as e:
            logging.getLogger("Lamia_unittest").debug(
                "error %s %s %s", e, parenttablename, parentfieldname
            )

        dbasetable = self.formtoolwidget.dbase.dbasetables[parenttablename]
        # get child index and combochild
        listparentcst = [
            dbasetable["fields"][field]["ParFldCst"]
            if "ParFldCst" in dbasetable["fields"][field].keys()
            else None
            for field in dbasetable["fields"].keys()
        ]

        if childfield is None:
            childfieldnames = [
                list(dbasetable["fields"].keys())[i]
                for i in range(len(listparentcst))
                if parentfieldname == listparentcst[i]
            ]
        else:
            childfieldnames = [childfield]

        if debug:
            print("**", listparentcst)
        if debug:
            print("***", childfieldnames)

        if comefromrawtable:
            listfieldname = [
                self.tableWidget.item(row, 0).text()
                for row in range(self.tableWidget.rowCount())
            ]
            for childfieldname in childfieldnames:
                if (
                    dbasetable["fields"][parentfieldname]["PGtype"] == "INT"
                    and parentcstvalue != ""
                    and parentcstvalue is not None
                ):
                    parentcstvalue = int(parentcstvalue)
                listtoadd = [
                    value[0]
                    for value in dbasetable["fields"][childfieldname]["Cst"]
                    if parentcstvalue in value[2]
                ]
                indexchildintable = listfieldname.index(
                    parenttablename + "." + childfieldname
                )
                combochild = self.tableWidget.cellWidget(indexchildintable, 1)
                combochild.clear()
                if len(listtoadd) > 0:
                    combochild.addItems(listtoadd)
        else:
            for childfieldname in childfieldnames:
                if (
                    dbasetable["fields"][parentfieldname]["PGtype"] == "INT"
                    and parentcstvalue != ""
                    and parentcstvalue is not None
                ):
                    parentcstvalue = int(parentcstvalue)

                listtoadd = [
                    value[0]
                    for value in dbasetable["fields"][childfieldname]["Cst"]
                    if (value[2] is None or parentcstvalue in value[2])
                ]

                if debug:
                    print("****", listtoadd)

                if self.formtoolwidget.formtoolwidgetconfdict is not None:
                    wdgconfdict = self.formtoolwidget.formtoolwidgetconfdict
                else:
                    wdgconfdict = self.formtoolwidget.formtoolwidgetconfdictmain

                if childfieldname in wdgconfdict[parenttablename]["widgets"]:
                    reinitcombo = False
                    if combochild is None:
                        reinitcombo = True
                        combochild = wdgconfdict[parenttablename]["widgets"][
                            childfieldname
                        ]
                    combochild.clear()
                    if len(listtoadd) > 0:
                        combochild.addItems(listtoadd)
                    if reinitcombo:
                        combochild = None

    def ___________________actionsOnFeatureSelection(self):
        pass

    def getDictValuesForWidget(self, featurepk=None):
        columns = self.formtoolwidget.dbase.getColumns(
            self.formtoolwidget.DBASETABLENAME + "_qgis"
        )
        if len(columns) == 0:  # table without qgis view ex : graphdata, pointtopo
            columns = self.formtoolwidget.dbase.getColumns(
                self.formtoolwidget.DBASETABLENAME
            )

        if not featurepk:
            values = [None] * len(columns)
            resdict = dict(zip(columns, values))
        else:
            # sql = "SELECT * FROM {} WHERE pk_{} = {}".format(
            #     self.formtoolwidget.DBASETABLENAME + "_qgis",
            #     self.formtoolwidget.DBASETABLENAME.lower(),
            #     featurepk,
            # )
            # values = self.formtoolwidget.dbase.query(sql)[0]

            # resdict = dict(zip(columns, values))

            resdict = self.formtoolwidget.dbase.lamiaorm[
                self.formtoolwidget.DBASETABLENAME
            ].read(featurepk)
        for k, v in self.formtoolwidget.TABLEFILTERFIELD.items():
            resdict[k] = v
        # print("**", resdict)
        return resdict

    def getDictValuesForWidget_old(self, featurepk=None):
        columns = self.formtoolwidget.dbase.getColumns(
            self.formtoolwidget.DBASETABLENAME + "_qgis"
        )
        if len(columns) == 0:  # table without qgis view ex : graphdata, pointtopo
            columns = self.formtoolwidget.dbase.getColumns(
                self.formtoolwidget.DBASETABLENAME
            )

        if not featurepk:
            values = [None] * len(columns)
        else:
            sql = "SELECT * FROM {} WHERE pk_{} = {}".format(
                self.formtoolwidget.DBASETABLENAME + "_qgis",
                self.formtoolwidget.DBASETABLENAME.lower(),
                featurepk,
            )
            values = self.formtoolwidget.dbase.query(sql)[0]

        resdict = dict(zip(columns, values))
        for k, v in self.formtoolwidget.TABLEFILTERFIELD.items():
            resdict[k] = v

        print("**", resdict)

        return resdict

    def applyResultDict(self, resultdict, checkifinforgottenfield=True):

        if self.formtoolwidget.mainifacewidget.interfacemode in [0, 1]:
            for (
                tablename,
                tabledict,
            ) in self.formtoolwidget.formtoolwidgetconfdict.items():
                for field, fieldwdg in tabledict["widgets"].items():
                    if not field in resultdict.keys():
                        if checkifinforgottenfield:
                            logging.getLogger("Lamia_unittest").debug(
                                "%s : field %s-%s not found in dictconf : %s",
                                self.formtoolwidget.DBASETABLENAME,
                                tablename,
                                field,
                                resultdict.keys(),
                            )
                        continue
                        # raise ValueError

                    self.setValueInWidget(fieldwdg, resultdict[field], tablename, field)

    def showImageinLabelWidget(self, wdg, savedfile):
        """
        Show the image file in the text widget
        Manage thumbnail image

        :param wdg: the text widget
        :param savedfile: the image file

        """
        notfound = True
        wdg.clear()

        if isinstance(savedfile, str):
            filetoshow = self.formtoolwidget.dbase.completePathOfFile(savedfile)
            possiblethumbnail, ext = os.path.splitext(filetoshow)
            # print(
            #     possiblethumbnail + "_thumbnail.png",
            #     len(possiblethumbnail + "_thumbnail.png"),
            # )
            if os.path.isfile(possiblethumbnail + "_thumbnail.png"):
                filetoshow = possiblethumbnail + "_thumbnail.png"

            if os.path.isfile(filetoshow):
                # wdg.clear()
                notfound = False
                wdg.setPixmap(filetoshow)
        elif isinstance(savedfile, bytes):  # from sptialite
            # wdg.clear()
            notfound = False
            wdg.setPixmap(savedfile)
        elif isinstance(savedfile, memoryview):  # from postgis
            notfound = False
            wdg.setPixmap(savedfile.tobytes())

        if notfound:
            wdg.setText("Image non trouvee")

    def ___________________actionsOnFeatureSave(self):
        pass

    def saveFeature(self, featurepk=None):

        dbasetablehasgeomfield = self.formtoolwidget.dbase.dbasetables[
            self.formtoolwidget.DBASETABLENAME
        ].get("geom", None)
        geometryskip = False
        if (
            hasattr(self.formtoolwidget, "GEOMETRYSKIP")
            and self.formtoolwidget.GEOMETRYSKIP
        ):
            geometryskip = True
        # print('dbasetablehasgeomfield',self.formtoolwidget.DBASETABLENAME, dbasetablehasgeomfield)
        if (
            dbasetablehasgeomfield is not None
            and featurepk is None
            and self.formtoolwidget.tempgeometry is None
            and not geometryskip
        ):  # assure taht a geometry is acquired on first creation
            self.formtoolwidget.mainifacewidget.connector.showErrorMessage(
                "Geometry needed"
            )
            return

        if (
            hasattr(self.formtoolwidget, "GEOMETRYSKIP")
            and self.formtoolwidget.GEOMETRYSKIP
        ):
            pass

        # savedfeaturepk = self.formtoolwidget.dbase.manageFeatureCreationOrUpdate(
        #     self.formtoolwidget.DBASETABLENAME, featurepk
        # )
        savedfeaturepk = self.formtoolwidget.dbase.lamiaorm[
            self.formtoolwidget.DBASETABLENAME
        ].create(featurepk)

        if not geometryskip:
            self.setGeometryToFeature(savedfeaturepk)
        self.saveFeatureProperties(savedfeaturepk)
        self.saveTABLEFILTERFIELD(savedfeaturepk)
        self.formtoolwidget.postSaveFeature(
            savedfeaturepk
        )  # featurepk toknow if new or not
        for lamiawidget in self.formtoolwidget.lamiawidgets:
            lamiawidget.postSaveFeature(savedfeaturepk)
        self.formtoolwidget.dbase.saveRessourceFile(
            self.formtoolwidget.DBASETABLENAME,
            savedfeaturepk,
            self.formtoolwidget.currentFeaturePK,
        )
        self._saveParentWidgetRelation(savedfeaturepk)

        # self.updateDateModification(savedfeaturepk)
        self._reinitAfterSaving()

        self.formtoolwidget.selectFeature(pk=savedfeaturepk)
        self._updateQgisLayerForSnapping()


    def setGeometryToFeature(self, featurepk=None):

        """
        Methode pour assigner le self.tempgeometry au self.currenfeature
        cree le self.currenfeature si besoin

        """

        # print('**', self.formtoolwidget.tempgeometry.asWkt())

        rawgeom = self.formtoolwidget.tempgeometry
        if rawgeom is None:  # geom no modified
            return

        processedgeom, success = self._convertGeomToProperGeom(rawgeom)
        # remove duplicate from linestring
        dbasetable = self.formtoolwidget.dbase.dbasetables[
            self.formtoolwidget.DBASETABLENAME
        ]
        processedgeom = self._removeDuplicatesFromGeom(processedgeom)
        self._setGeometryToFeature(featurepk=featurepk, qgsgeom=processedgeom)
        return True

    def _convertGeomToProperGeom(self, qgsgeom):
        dbasetable = self.formtoolwidget.dbase.dbasetables[
            self.formtoolwidget.DBASETABLENAME
        ]
        success = False
        if (
            qgsgeom is not None
            and dbasetable["geom"] in ["POINT", "LINESTRING", "POLYGON"]
            and qgsgeom.isMultipart()
        ):
            success = qgsgeom.convertToSingleType()
        elif (
            qgsgeom is not None
            and dbasetable["geom"] in ["MULTIPOLYGON"]
            and not qgsgeom.isMultipart()
        ):
            success = qgsgeom.convertToMultiType()

        if (
            dbasetable is not None
            and "geom" in dbasetable.keys()
            and dbasetable["geom"] == "LINESTRING"
            and qgsgeom is not None
            and qgsgeom.type() == 0
        ):  # case point in linestring layer
            qgsgeom = qgis.core.QgsGeometry.fromPolylineXY(
                [qgsgeom.asPoint(), qgsgeom.asPoint()]
            )
        return qgsgeom, success

    def _removeDuplicatesFromGeom(self, qgsgeom):
        dbasetable = self.formtoolwidget.dbase.dbasetables[
            self.formtoolwidget.DBASETABLENAME
        ]

        if qgsgeom is not None and dbasetable["geom"] in ["LINESTRING"]:
            geomaspoly = qgsgeom.asPolyline()
            geomfinal = [geomaspoly[0]]
            areNodesEqualsFct = self.formtoolwidget.dbase.utils.areNodesEquals
            if not areNodesEqualsFct(geomaspoly[0], geomaspoly[-1]):
                for index in range(len(geomaspoly) - 1):
                    if not areNodesEqualsFct(geomaspoly[index], geomaspoly[index + 1]):
                        geomfinal.append(geomaspoly[index + 1])
                qgsgeom = qgis.core.QgsGeometry.fromPolylineXY(geomfinal)
        return qgsgeom

    def _setGeometryToFeature(self, featurepk, qgsgeom):
        sqlqgsgeom = qgsgeom.asWkt()
        # sql = "UPDATE {} SET geom=ST_GeomFromText('{}',{}) WHERE pk_{}={}".format(
        #     self.formtoolwidget.DBASETABLENAME,
        #     sqlqgsgeom,
        #     self.formtoolwidget.dbase.crsnumber,
        #     self.formtoolwidget.DBASETABLENAME.lower(),
        #     featurepk,
        # )
        # self.formtoolwidget.dbase.query(sql)

        self.formtoolwidget.dbase.lamiaorm[self.formtoolwidget.DBASETABLENAME].update(
            featurepk, {"geom": sqlqgsgeom},
        )

    def _updateQgisLayerForSnapping(self):
        dbasetablename = self.formtoolwidget.DBASETABLENAME
        if dbasetablename in self.formtoolwidget.mainifacewidget.qgiscanvas.layers.keys():
            layer  = self.formtoolwidget.mainifacewidget.qgiscanvas.layers[dbasetablename]['layerqgis']
            layer.reload()

    def updateDateModification_old(self, featurepk):
        if "Objet" in self.formtoolwidget.dbase.getParentTable(
            self.formtoolwidget.DBASETABLENAME
        ):
            pkobjet = self.formtoolwidget.dbase.lamiaorm[
                self.formtoolwidget.DBASETABLENAME.lower()
            ].read(featurepk)["pk_objet"]
            # pkobjet = self.formtoolwidget.dbase.getValuesFromPk(
            #     self.formtoolwidget.DBASETABLENAME.lower() + "_qgis ",
            #     "pk_objet",
            #     featurepk,
            # )

            datemodif = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.formtoolwidget.dbase.lamiaorm[
                self.formtoolwidget.DBASETABLENAME.lower()
            ].update(featurepk, {"datetimemodification": datemodif})
            # sql = (
            #     "UPDATE Objet SET datetimemodification = '"
            #     + datemodif
            #     + "'  WHERE pk_objet = "
            #     + str(pkobjet)
            # )
            # self.formtoolwidget.dbase.query(sql)

    def saveFeatureProperties(self, featurepk=None):
        """
        Method called by saveFeature

        Method for saving feature properties of the ui in the tables
        """

        debug = False

        if self.formtoolwidget.mainifacewidget.interfacemode in [0, 1]:
            if self.formtoolwidget.formtoolwidgetconfdict is None:
                return

            resdict = {}
            for (
                tablename,
                tabledict,
            ) in self.formtoolwidget.formtoolwidgetconfdict.items():
                if len(tabledict["widgets"].keys()) == 0:
                    continue
                for fieldname, fieldwdg in tabledict["widgets"].items():
                    fieldvaluetosave = self.getValueFromWidget(
                        fieldwdg, tablename, fieldname
                    )
                    # if fieldvaluetosave is not None:
                    if self.formtoolwidget.dbase.utils.isAttributeNull(
                        fieldvaluetosave
                    ):
                        resdict[fieldname] = None
                        # resdict[fieldname] = "NULL"
                    else:
                        resdict[fieldname] = fieldvaluetosave

            self.formtoolwidget.dbase.lamiaorm[
                self.formtoolwidget.DBASETABLENAME
            ].update(featurepk, resdict)

    def saveFeatureProperties_old(self, featurepk=None):
        """
        Method called by saveFeature

        Method for saving feature properties of the ui in the tables
        """

        debug = False

        if self.formtoolwidget.mainifacewidget.interfacemode in [0, 1]:
            if self.formtoolwidget.formtoolwidgetconfdict is None:
                return

            resdict = {}
            for (
                tablename,
                tabledict,
            ) in self.formtoolwidget.formtoolwidgetconfdict.items():
                if len(tabledict["widgets"].keys()) == 0:
                    continue
                # get field values
                result = []
                for fieldname, fieldwdg in tabledict["widgets"].items():
                    fieldvaluetosave = self.getValueFromWidget(
                        fieldwdg, tablename, fieldname
                    )
                    if fieldvaluetosave is not None:
                        resdict[fieldname] = fieldvaluetosave
                        result.append(fieldvaluetosave)
                    else:
                        result.append(None)

                # get tablepk
                tablepk = self.formtoolwidget.dbase.getValuesFromPk(
                    self.formtoolwidget.DBASETABLENAME + "_qgis",
                    "pk_" + tablename.lower(),
                    featurepk,
                )
                """
                sql = "SELECT pk_" + str(tablename).lower() + " FROM " + str(self.dbasetablename).lower() + "_qgis"
                sql += "  WHERE pk_" + self.dbasetablename.lower() + " = " + str(self.currentFeaturePK)
                tablepk = self.dbase.query(sql)[0][0]
                """

                # update sql
                fieldnames = tabledict["widgets"].keys()
                sql = "UPDATE " + str(tablename).lower() + " SET "
                for i, field in enumerate(fieldnames):
                    print(field, result[i])
                    if isinstance(result[i], str) or isinstance(result[i], unicode):
                        if result[i] != "":
                            resultstring = result[i]
                            if "'" in resultstring:
                                resultstring = "''".join(resultstring.split("'"))
                            resulttemp = "'" + resultstring + "'"
                        else:
                            resulttemp = "NULL"
                    elif result[i] is None:
                        resulttemp = "NULL"
                    else:
                        # print(type(result[i ]))
                        resulttemp = str(result[i])

                    sql += str(field) + " = " + resulttemp + ","

                sql = sql[:-1]  # remove last ,

                sql += " WHERE pk_" + str(tablename) + " = " + str(tablepk)
                self.formtoolwidget.dbase.query(sql)

            # print("**", resdict)

    def setValueInWidget(self, wdg, valuetoset, table, field):
        """
        Called by initFeatureProperties when iterating the fields

        :param wdg:         the widget to set a value to
        :param valuetoset:  the value
        :param table:       the table of the value
        :param field:       the field of the value
        """

        # logging.getLogger("Lamia_unittest").debug(
        #     "init  %s %s %s %s", wdg.objectName(), str(valuetoset), table, field
        # )

        if isinstance(wdg, list):
            for subwdg in wdg:
                self.setValueInWidget(subwdg, valuetoset, table, field)
            return

        if isinstance(wdg, QTextEdit) or isinstance(wdg, QLineEdit):
            if valuetoset is not None:
                wdg.setText(str(valuetoset))
            else:
                wdg.setText("")
        elif isinstance(wdg, QSpinBox) or isinstance(wdg, QDoubleSpinBox):
            try:
                if valuetoset is not None:
                    wdg.setValue(valuetoset)
                else:
                    wdg.setValue(-1)
            except Exception as e:
                logging.getLogger("Lamia_unittest").debug(
                    "error %s %s %s %s", table, field, str(valuetoset), e
                )
        elif isinstance(wdg, QComboBox):
            try:
                if valuetoset is not None:
                    text = self.formtoolwidget.dbase.getConstraintTextFromRawValue(
                        table, field, valuetoset
                    )
                    index = wdg.findText(text)
                    wdg.setCurrentIndex(index)
                else:
                    wdg.setCurrentIndex(0)
            except Exception as e:
                logging.getLogger("Lamia_unittest").debug(
                    "error %s %s %s", table, field, e
                )
        elif isinstance(wdg, QDateEdit):
            if valuetoset is not None:
                if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                    wdg.setDateTime(
                        QtCore.QDateTime.fromString(valuetoset, "yyyy-MM-dd")
                    )

                elif isinstance(valuetoset, QtCore.QDate):
                    wdg.setDate(valuetoset)
            else:
                wdg.setSpecialValueText(" ")
                wdg.setDate(QtCore.QDate.fromString("0001-01-01", "yyyy-MM-dd"))

        elif isinstance(wdg, QDateTimeEdit):
            if valuetoset is not None:
                if isinstance(valuetoset, str) or isinstance(valuetoset, unicode):
                    wdg.setDateTime(
                        QtCore.QDateTime.fromString(valuetoset, "yyyy-MM-dd hh:mm:ss")
                    )

                elif isinstance(valuetoset, QtCore.QDate):
                    wdg.setDate(valuetoset)
                elif isinstance(valuetoset, datetime.datetime):
                    wdg.setDateTime(
                        QtCore.QDateTime.fromString(
                            str(valuetoset), "yyyy-MM-dd hh:mm:ss"
                        )
                    )
            else:
                wdg.setSpecialValueText(" ")
                wdg.setDate(QtCore.QDate.fromString("0001-01-01", "yyyy-MM-dd"))

        elif isinstance(wdg, QCheckBox):
            if valuetoset is not None:
                if valuetoset:
                    wdg.setCheckState(2)
                else:
                    wdg.setCheckState(0)
            else:
                wdg.setCheckState(0)

        elif isinstance(wdg, QLabel):
            if valuetoset is not None:
                if (
                    "Cst"
                    in self.formtoolwidget.dbase.dbasetables[table]["fields"][
                        field
                    ].keys()
                ):
                    wdg.setText(
                        self.formtoolwidget.dbase.getConstraintTextFromRawValue(
                            table, field, valuetoset
                        )
                    )
                else:
                    wdg.setText(valuetoset)
            else:
                wdg.setText("")

    def getValueFromWidget(self, wdg, tablename, fieldname):
        """
        Method to obtain the savable value of a property widget

        :param wdg: the property widget
        :param tablename: the table name  linked with th widget
        :param fieldname: the field name  linked with th widget
        :return: The value of the widget, in good format for saving
        """

        fieldvaluetosave = None
        if "Cst" in self.formtoolwidget.dbase.dbasetables[tablename]["fields"][
            fieldname
        ].keys() and not isinstance(wdg, str):
            try:
                if isinstance(wdg, list):
                    wdg = wdg[0]
                fieldvaluetosave = self.formtoolwidget.dbase.getConstraintRawValueFromText(
                    tablename, fieldname, wdg.currentText()
                )
            except Exception as e:
                print("error getValueFromWidget", tablename, fieldname, e)
            if fieldvaluetosave == "":
                fieldvaluetosave = None
        else:
            if isinstance(wdg, list):
                wdg = wdg[0]
            if isinstance(wdg, QSpinBox) and wdg.value() > -1:
                fieldvaluetosave = int(wdg.value())
            elif isinstance(wdg, QDoubleSpinBox) and wdg.value() > -1:
                fieldvaluetosave = float(wdg.value())
            elif isinstance(wdg, QTextEdit) or isinstance(wdg, QTextBrowser):
                fieldvaluetosave = wdg.toPlainText()
            elif isinstance(wdg, QLineEdit):
                fieldvaluetosave = wdg.text()
            elif isinstance(wdg, QCheckBox):
                value = wdg.checkState()
                if int(value):
                    fieldvaluetosave = 1
                else:
                    fieldvaluetosave = 0
            elif isinstance(wdg, QDateEdit) and wdg.findChild(QLineEdit).text() != " ":
                fieldvaluetosave = wdg.date().toString("yyyy-MM-dd")
            elif (
                isinstance(wdg, QDateTimeEdit)
                and wdg.findChild(QLineEdit).text() != " "
            ):
                fieldvaluetosave = wdg.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            elif isinstance(wdg, str):
                fieldvaluetosave = wdg

        return fieldvaluetosave

    """
    def saveRessourceFile(self,featurepk=None):


        if not 'Ressource' in self.formtoolwidget.dbase.getParentTable(self.formtoolwidget.DBASETABLENAME):
            return
            
        DBASETABLENAMElower = self.formtoolwidget.DBASETABLENAME.lower()
        result = self.formtoolwidget.dbase.getValuesFromPk(DBASETABLENAMElower + "_qgis",
                                                            'datetimecreation',
                                                            featurepk)

        if result is not None:
            datevalue = datetime.datetime.strptime(str(result), "%Y-%m-%d %H:%M:%S").date()
            if isinstance(datevalue, datetime.date):
                datevalue = datevalue.strftime('%Y-%m-%d')
        else:
            return

        date = ''.join(datevalue.split('-'))

        result = self.formtoolwidget.dbase.getValuesFromPk(DBASETABLENAMElower + "_qgis",
                                                            ['pk_ressource', 'id_ressource', 'file'],
                                                            featurepk)
        if len(result) > 0:
            pkressource, idressource, resfile = result
        else:
            return

        dbaseressourcesdirectory = self.formtoolwidget.dbase.dbaseressourcesdirectory
        if resfile is not None and len(resfile) > 0:
            if resfile[0] == '.':
                resfile = os.path.join(dbaseressourcesdirectory,resfile)
            else:
                if os.path.isfile(resfile):
                    filename = os.path.basename(resfile)
                    filename = str(idressource) + '_' + filename
                    destinationdir = os.path.join(dbaseressourcesdirectory,self.formtoolwidget.DBASETABLENAME,date)
                    destinationfile = os.path.join(destinationdir, filename)

                    self.formtoolwidget.dbase.copyRessourceFile(fromfile= resfile,
                                                                tofile=destinationfile,
                                                                withthumbnail=0,
                                                                copywholedirforraster=False)


                    finalname = os.path.join('.',os.path.relpath(destinationfile, dbaseressourcesdirectory ))
                    sql = "UPDATE Ressource SET file = '" + finalname + "' WHERE pk_ressource = " +  str(pkressource) + ";"
                    query = self.formtoolwidget.dbase.query(sql)

                    #removing old file 
                    #if self.beforesavingFeature is not None:
                    if self.formtoolwidget.currentFeaturePK is not None:   #case updating existing feature
                        sql = "SELECT file FROM Ressource  WHERE pk_ressource = " + str(pkressource) + ";"
                        query = self.formtoolwidget.dbase.query(sql)
                        result = [row[0] for row in query]
                        oldfile = result[0]
                    else:
                        oldfile = ''

                    newfile = finalname

                    if os.path.isfile(self.formtoolwidget.dbase.completePathOfFile(oldfile)) and oldfile != newfile:
                        os.remove(self.formtoolwidget.dbase.completePathOfFile(oldfile))
                    else:
                        pass
    """

    def _saveParentWidgetRelation(self, featurepk=None):

        debug = False
        if debug:
            self.formtoolwidget.dbase.printsql = True
        if (
            self.formtoolwidget.currentFeaturePK == featurepk
        ):  # relation is already saved
            return

        if (
            hasattr(self.formtoolwidget, "PARENTJOIN")
            and self.formtoolwidget.parentWidget is not None
        ):
            parenttblname = self.formtoolwidget.parentWidget.DBASETABLENAME
            childtblname = self.formtoolwidget.DBASETABLENAME
            parentjoin = self.formtoolwidget.PARENTJOIN
            if parenttblname in self.formtoolwidget.PARENTJOIN.keys():
                joindict = self.formtoolwidget.PARENTJOIN[parenttblname]
                if joindict["tctable"] is None:
                    parentcolval = self.formtoolwidget.dbase.getValuesFromPk(
                        parenttblname + "_qgis",
                        joindict["colparent"],
                        self.formtoolwidget.parentWidget.currentFeaturePK,
                    )
                    childparenttables = [
                        childtblname
                    ] + self.formtoolwidget.dbase.getParentTable(childtblname)
                    for tablename in childparenttables:
                        dbasetable = self.formtoolwidget.dbase.dbasetables[tablename]
                        if joindict["colthistable"] in dbasetable["fields"].keys():
                            pktable = self.formtoolwidget.dbase.getValuesFromPk(
                                childtblname + "_qgis",
                                "pk_" + tablename.lower(),
                                featurepk,
                            )
                            # sql = "UPDATE {} SET {} = {} WHERE pk_{} = {}".format(
                            #     tablename,
                            #     joindict["colthistable"],
                            #     parentcolval,
                            #     tablename.lower(),
                            #     pktable,
                            # )
                            # self.formtoolwidget.dbase.query(sql)

                            self.formtoolwidget.dbase.lamiaorm[tablename].update(
                                pktable, {joindict["colthistable"]: parentcolval}
                            )

                            break

                else:
                    fieldtcthis = self.formtoolwidget.dbase.getValuesFromPk(
                        childtblname + "_qgis", joindict["colthistable"], featurepk
                    )
                    fieldtcparent = self.formtoolwidget.dbase.getValuesFromPk(
                        parenttblname + "_qgis",
                        joindict["colparent"],
                        self.formtoolwidget.parentWidget.currentFeaturePK,
                    )
                    # sql = (
                    #     "INSERT INTO {}(lpk_revision_begin,{},{}) "
                    #     "VALUES({},{},{})".format(
                    #         joindict["tctable"],
                    #         joindict["tctablecolparent"],
                    #         joindict["tctablecolthistable"],
                    #         self.formtoolwidget.dbase.maxrevision,
                    #         fieldtcparent,
                    #         fieldtcthis,
                    #     )
                    # )
                    # self.formtoolwidget.dbase.query(sql)
                    res = self.formtoolwidget.dbase.lamiaorm[joindict["tctable"]][
                        f"{joindict['tctablecolparent']} = {fieldtcparent} AND {joindict['tctablecolthistable']} = {fieldtcthis} AND lpk_revision_end IS NULL"
                    ]
                    if not res:
                        valdict = {
                            "lpk_revision_begin": self.formtoolwidget.dbase.maxrevision,
                            joindict["tctablecolparent"]: fieldtcparent,
                            joindict["tctablecolthistable"]: fieldtcthis,
                        }
                        pk = self.formtoolwidget.dbase.lamiaorm[
                            joindict["tctable"]
                        ].create()
                        self.formtoolwidget.dbase.lamiaorm[joindict["tctable"]].update(
                            pk, valdict
                        )

        if debug:
            self.formtoolwidget.dbase.printsql = False
        # self.dbase.commit()

    def saveTABLEFILTERFIELD(self, featurepk=None):
        if len(self.formtoolwidget.TABLEFILTERFIELD) > 0:
            parenttables = [self.formtoolwidget.DBASETABLENAME]
            parenttables += self.formtoolwidget.dbase.getParentTable(
                self.formtoolwidget.DBASETABLENAME
            )
            for tablename in parenttables:
                fields = self.formtoolwidget.dbase.dbasetables[tablename]["fields"]
                tablepk = self.formtoolwidget.dbase.getValuesFromPk(
                    self.formtoolwidget.DBASETABLENAME + "_qgis",
                    "pk_" + tablename.lower(),
                    featurepk,
                )
                for (
                    fieldname,
                    fieldvalue,
                ) in self.formtoolwidget.TABLEFILTERFIELD.items():
                    if fieldname in fields:
                        if isinstance(fieldvalue, str):
                            fieldvalue = "'" + fieldvalue + "'"
                        sql = "UPDATE {} SET {} = {} WHERE pk_{} = {}".format(
                            tablename, fieldname, fieldvalue, tablename.lower(), tablepk
                        )
                        self.formtoolwidget.dbase.query(sql)

    def _reinitAfterSaving(self):
        # reinit

        layergeomtype = self.formtoolwidget.mainifacewidget.qgiscanvas.layers[
            self.formtoolwidget.DBASETABLENAME
        ]["layer"].geometryType()
        # self.formtoolwidget.mainifacewidget.qgiscanvas.createorresetRubberband(layergeomtype)
        self.formtoolwidget.tempgeometry = None
        layer = self.formtoolwidget.mainifacewidget.qgiscanvas.layers[
            self.formtoolwidget.DBASETABLENAME
        ]["layerqgis"]
        # layer.dataProvider().forceReload()
        layer.dataProvider().reloadData()
        layer.repaintRequested.emit()

        # self.mainifacewidget.qgiscanvas.canvas.refresh()

    def ___________________actionsOnDeletingFeature(self):
        pass

    def deleteFeature(self):
        if self.formtoolwidget.dbase.base3version:
            pkobjet, revobjet = self.formtoolwidget.dbase.getValuesFromPk(
                self.formtoolwidget.DBASETABLENAME + "_qgis",
                ["pk_object", "lpk_revision_begin"],
                self.formtoolwidget.currentFeaturePK,
            )
        else:
            pkobjet, revobjet = self.formtoolwidget.dbase.getValuesFromPk(
                self.formtoolwidget.DBASETABLENAME + "_qgis",
                ["pk_objet", "lpk_revision_begin"],
                self.formtoolwidget.currentFeaturePK,
            )
        # if revobjet == self.formtoolwidget.dbase.maxrevision:

        self.formtoolwidget.dbase.lamiaorm[self.formtoolwidget.DBASETABLENAME].delete(
            self.formtoolwidget.currentFeaturePK
        )

        # tablestodel = [self.formtoolwidget.DBASETABLENAME]
        # tablestodel += self.formtoolwidget.dbase.getParentTable(
        #     self.formtoolwidget.DBASETABLENAME
        # )
        # pkfields = ["pk_" + tablename.lower() for tablename in tablestodel]

        # for tablename in tablestodel:
        #     pkvalues = self.formtoolwidget.dbase.getValuesFromPk(
        #         self.formtoolwidget.DBASETABLENAME + "_qgis",
        #         pkfields,
        #         self.formtoolwidget.currentFeaturePK,
        #     )
        # dictdelete = dict(zip(tablestodel, pkvalues))  # dict : {tablename : pkvalue}
        # for tablename, pkvalue in dictdelete.items():
        #     sql = "DELETE FROM {} WHERE pk_{} = {}".format(
        #         tablename, tablename.lower(), str(pkvalue)
        #     )
        #     self.formtoolwidget.dbase.query(sql)
        self.formtoolwidget.postDeleteFeature()
        """
        else:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "UPDATE Objet SET lpk_revision_end = " + str(self.formtoolwidget.dbase.maxrevision)
            sql += " , datetimedestruction = '" + str(datesuppr) + "'"
            sql += " , datetimemodification = '" + str(datesuppr) + "'"
            sql += " WHERE pk_objet = " + str(pkobjet)
            self.dbase.query(sql)
        """

    def archiveFeature(self):
        datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.formtoolwidget.dbase.lamiaorm[self.formtoolwidget.DBASETABLENAME].update(
            self.formtoolwidget.currentFeaturePK, {"datetimedestruction": datesuppr}
        )
        # pkobjet, revobjet = self.formtoolwidget.dbase.getValuesFromPk(
        #     self.formtoolwidget.DBASETABLENAME + "_qgis",
        #     ["pk_object", "lpk_revision_begin"],
        #     self.formtoolwidget.currentFeaturePK,
        # )
        # # if revobjet == self.formtoolwidget.dbase.maxrevision:
        # # idobjet = self.currentFeature['id_objet']
        # # datesuppr = QtCore.QDate.fromString(str(datetime.date.today()), 'yyyy-MM-dd').toString('yyyy-MM-dd')
        # datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # sql = (
        #     "UPDATE object SET datetimedestruction = '"
        #     + datesuppr
        #     + "'  WHERE pk_object = "
        #     + str(pkobjet)
        #     + ";"
        # )
        # self.formtoolwidget.dbase.query(sql)
        """
        else:
            datesuppr = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sql = "UPDATE Objet SET lpk_revision_end = " + str(self.formtoolwidget.dbase.maxrevision)
            sql += " , datetimedestruction = '" + str(datesuppr) + "'"
            sql += " , datetimemodification = '" + str(datesuppr) + "'"
            sql += " WHERE pk_objet = " + str(pkobjet)
            self.dbase.query(sql)
        """

    def ___________________utilsFunctions(self):
        pass

    def getQgsGeomFromPk(self, pk):
        """Return a QgsGeometry from pk using formwidget table defined in DBASETABLENAME

        :param pk: primary key
        :type pk: int
        :return: The QgsGeometry 
        :rtype: QgsGeometry
        """
        wkt = self.formtoolwidget.dbase.getWktGeomFromPk(
            self.formtoolwidget.DBASETABLENAME, pk
        )
        geom = qgis.core.QgsGeometry.fromWkt(wkt)
        return geom

    def mergeQtWidgets(self, wdg1, wdg2):
        """Enable merging of widget - wd2.xxx can be reached with wdg1.xxx

        :param wdg1: parent widget to merge
        :type wdg1: QtWidget
        :param wdg2: childwidget to merge
        :type wdg2: QtWidget
        """
        finaldict = {}
        for key, val in wdg2.__dict__.items():
            if type(val) in [
                QComboBox,
                QTextEdit,
                QLineEdit,
                QSpinBox,
                QDoubleSpinBox,
                QDateEdit,
                QDateTimeEdit,
                QTextBrowser,
                QCheckBox,
                # QLabel,
                # QTabWidget,
                # QTabBar,
                QStackedWidget,
                QToolButton,
                QPushButton,
            ]:
                finaldict[key] = val
        wdg1.__dict__ = {**wdg1.__dict__, **finaldict}

