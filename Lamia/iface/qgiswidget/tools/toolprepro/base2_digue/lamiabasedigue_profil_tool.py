# -*- coding: utf-8 -*-

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


from ..base2.lamiabase_profil_tool import BaseProfilTool


class BaseDigueProfilTool(BaseProfilTool):


    def __init__(self, **kwargs):
        super(BaseDigueProfilTool, self).__init__(**kwargs)

    """
    def initTool(self):
        super(BaseDigueProfilTool, self).initTool()
        self.linkagespec = {'Infralineaire' : {'tabletc' : None,
                                              'idsource' : 'lid_descriptionsystem',
                                            'idtcsource' : None,
                                           'iddest' : 'id_descriptionsystem',
                                           'idtcdest' : None,
                                           'desttable' : ['Infralineaire']} }
    """


    def initMainToolWidget(self):

        super(BaseDigueProfilTool,self).initMainToolWidget()

        # parent widgets
        if self.parentWidget is not None and self.parentWidget.DBASETABLENAME in ['Infralineaire']:
            self.toolwidgetmain.pushButton_setasdefault.clicked.connect(self.setAsDefault)
        else:
            self.toolwidgetmain.pushButton_setasdefault.setParent(None)







    def setAsDefault(self):
        print('fdedee',self.parentWidget.currentFeature)
        if self.parentWidget.currentFeaturePK is not None:

            currentwdg = self.dbasechildwdgfield[self.userwdgfield.stackedWidget.currentIndex()]

            if currentwdg.currentFeaturePK is not None:
                #idressoruce
                sql = "SELECT id_ressource FROM " + currentwdg.DBASETABLENAME.lower() + "_qgis"
                sql += " WHERE pk_" + currentwdg.DBASETABLENAME.lower() + " = " + str(self.currentFeaturePK)
                idressource = self.dbase.query(sql)[0][0]

                pkparentfeature = self.parentWidget.currentFeaturePK

                sql = "UPDATE " + str(self.parentWidget.DBASETABLENAME.lower()) + " SET  lid_ressource_4 = " + str(idressource)
                sql += " WHERE pk_"+ str(self.parentWidget.DBASETABLENAME.lower()) + " = " + str(pkparentfeature)
                query = self.dbase.query(sql)
                self.dbase.commit()

