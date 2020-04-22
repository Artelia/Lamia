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



import os
import io
import sys
import numpy as np
import logging


class CostCore():

    POSTPROTOOLNAME = 'costtools'

    def __init__(self, dbaseparser,messageinstance=None):

        self.dbase = dbaseparser
        self.messageinstance = messageinstance

        self.confdataplugin = os.path.join(os.path.dirname(__file__), self.dbase.worktype.lower())
        self.confdataproject = os.path.join(self.dbase.dbaseressourcesdirectory, 'config', self.POSTPROTOOLNAME)
        self.logger = logging.getLogger("Lamia_unittest")

    def runCost(self, costfilepath,pkzonegeos=[]):
        debug = True
        if os.path.isfile(costfilepath):  #complete path is given in exportconffilepath
            tabletypepath = costfilepath
        else:   #just filename is given in exportconffilepath
            tabletypepath = os.path.join(self.confdataplugin, costfilepath + '.csv')

        bordereau = self.readBordereau(tabletypepath)
        if debug : self.logger.debug('***** bordereau : *****')
        if debug : self.logger.debug('%s', bordereau)

        restot = self.buildSQL(bordereau, pkzonegeos)
        if debug : self.logger.debug('***** restot : *****')
        if debug : self.logger.debug('%s', restot)

        ressql, resultfinal = self.priceCalculus(bordereau,restot)
        if debug : self.logger.debug('***** ressql : *****')
        if debug : self.logger.debug('%s', ressql)
        if debug : self.logger.debug('***** resultfinal : *****')
        if debug : self.logger.debug('%s',resultfinal)
        
        return bordereau, ressql, resultfinal 


    def readBordereau(self, costfilepath):
        debug = False

        costfile = open(costfilepath, "r")
        lines = costfile.readlines()
        costfile.close()
        bordereau = {}
        bordereau['condition'] = None
        bordereau['price'] = None
        bordereau['prix'] =  []
        bordereau['fields'] = []
        linecourread = False
        for i, line in enumerate(lines):
            # print(linecourread, line)
            if i == 0:
                bordereau['sql'] = line.split(';')[0].strip()
                continue

            if not linecourread and line.split(';')[0] == '':
                continue
            elif not linecourread and line.split(';')[0] != '':
                linecourread = True
                linesplitted = line.split(';')
                for elem in linesplitted:
                    if elem.split(',')[0].strip() == 'Prix':
                        if len(elem.split(','))>1:
                            bordereau['prix'].append(elem.split(',')[1].strip())
                        else:
                            bordereau['prix'].append(None)
                    else:
                        bordereau['fields'].append(elem.strip())



                continue

            if linecourread:
                #bordereau['case'].append(line.split(';'))
                linesplitted = line.strip().split(';')
                lineprice = [float(val) if val != '' else None for val in linesplitted[0:len(bordereau['prix'])]]
                linecondition = linesplitted[len(bordereau['prix']):]

                #print(lineprice,linecondition )

                if bordereau['condition'] is None:
                    bordereau['condition'] = np.array([linecondition])
                    bordereau['price'] = np.array([lineprice])
                else:
                    bordereau['condition'] = np.append(bordereau['condition'],[linecondition], axis=0 )
                    bordereau['price'] = np.append(bordereau['price'], [lineprice], axis=0)

        if debug: self.logger.debug('bordereau')
        if debug: self.logger.debug('%s', str(bordereau))

        return bordereau

        


    def buildSQL(self, bordereau, pkzonegeos):
        debug = True

        if self.dbase.__class__.__name__ == 'SpatialiteDBaseParser':
            sql = "SELECT CreateSpatialIndex('Infralineaire', 'geom')"
            self.dbase.query(sql)

        lenlinecondition = len(list(bordereau['condition']))
        #print('lenlinecondition',lenlinecondition)

        fields = ', '.join(bordereau['fields'])
        #print(fields)
        sqlfinal = bordereau['sql'].replace('*',fields )

        sqlsplitted = self.dbase.utils.splitSQLSelectFromWhereOrderby(sqlfinal)
        #wheresql = self.getcombotypeitemsWhereClause()
        if pkzonegeos:
            wheresql = "Zonegeo_now.pk_zonegeo IN ({})".format(' ,'.join([str(pk) for pk in pkzonegeos]))

            if 'WHERE' in sqlsplitted.keys():
                sqlsplitted['WHERE'] += ' AND ' + wheresql
            else:
                sqlsplitted['WHERE'] = wheresql
        sqlfinal = self.dbase.utils.rebuildSplittedQuery(sqlsplitted)

        if False:
            if idszonegeoselected is not None:
                sqlsplitted = self.dbase.splitSQLSelectFromWhereOrderby(sqlfinal)
                wheresql = 'id_zonegeo IN (' + ','.join(idszonegeoselected) + ')'
                if 'WHERE' in sqlsplitted.keys():
                    sqlsplitted['WHERE'] += ' AND ' + wheresql
                else:
                    sqlsplitted['WHERE'] = wheresql

                sqlfinal = self.dbase.rebuildSplittedQuery(sqlsplitted)

        if debug: self.logger.debug('sql : %s',sqlfinal )

        sqlfinal = self.dbase.updateQueryTableNow(sqlfinal)

        if debug: self.logger.debug('sql : %s', sqlfinal)

        restot = self.dbase.query(sqlfinal)

        if debug: self.logger.debug('res : %s', str(restot))

        if self.dbase.__class__.__name__ == 'SpatialiteDBaseParser':
            sql = "SELECT DisableSpatialIndex('Infralineaire', 'geom')"
            self.dbase.query(sql)

        return restot
        #self.priceCalculus(restot)




    def priceCalculus(self, bordereau, restot):
        ressql=[]
        resultfinal=[]
        debug = False
        if debug : self.logger.debug('Start')

        for i, res in enumerate(restot):
            if False and debug and i>9:
                break

            restrunc = res[:-1]
            ressql.append(restrunc)
            force = None
            indexconditionline = None

            for j, linecondition in enumerate(bordereau['condition']):

                indexwherenull = np.where(linecondition=='')
                #print(indexwherenull)

                linesimplified = np.delete(linecondition, indexwherenull)
                ressimplified = np.delete(restrunc, indexwherenull)

                # if debug: self.logger.debug('lineres %s, linecond %s',linesimplified, ressimplified )

                #test if array equal
                arrayequal = False
                for k, tabelem in enumerate(linesimplified):
                    if ('<' in tabelem or '>' in tabelem) and ressimplified[k] is not None:
                        tempbool = eval(str(ressimplified[k]) + str(tabelem))
                        #print('eval', str(ressimplified[k]) + str(tabelem),tempbool)
                        if tempbool:
                            arrayequal = True
                        else:
                            arrayequal = False
                            break
                    else:
                        if ressimplified[k] == tabelem :
                            arrayequal = True
                        else:
                            arrayequal = False
                            break

                if arrayequal:
                    if force is None:
                        force = len(linesimplified)
                        indexconditionline = j
                    else:
                        if len(linesimplified) > force:
                            force = len(linesimplified)
                            indexconditionline = j



                if False:
                    if np.array_equal(linesimplified, ressimplified):
                        if force is None:
                            force = len(linesimplified)
                            indexconditionline = j
                        else:
                            if len(linesimplified)>force:
                                force = len(linesimplified)
                                indexconditionline = j

            #print('force',force,  indexconditionline)


            #price
            field = restrunc    #used in eval
            prices = bordereau['price'][indexconditionline]
            resultprices = []
            if indexconditionline is not None:
                if debug: self.logger.debug('line %s, cond %s', restrunc,bordereau['condition'][indexconditionline])

                for j, val in enumerate(bordereau['prix']):
                    if val is None:
                        resultprices.append(prices[j])
                    else:
                        stringtoeval = str(prices[j]) + val
                        # print('stringtoeval', stringtoeval)
                        try:
                            valeval = eval(stringtoeval)
                            #print('eval', valeval)
                            if valeval>0:
                                resultprices.append(valeval)
                            else:
                                resultprices.append(None)
                        except Exception as e:
                            #print('ex', e)
                            resultprices.append(None)
            else:
                if debug: self.logger.debug('line %s, cond %s', restrunc,'No condition')
                resultprices = [None]*len(bordereau['prix'])

            #finalprice
            finalprice = next(iter(item for item in resultprices[::-1] if item is not None),None)

            if debug: self.logger.debug('prices %s, finalprice %s', resultprices, finalprice)

            resultfinal.append(finalprice)

            if debug: self.logger.debug('resultfinal %s',str(resultfinal))
        
        return ressql, resultfinal
        #self.writeResultsInTable(ressql, resultfinal)

