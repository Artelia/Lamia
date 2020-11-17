# -*- coding: utf-8 -*-

import qgis
from qgis.PyQt import QtCore

settings = QtCore.QSettings( QtCore.QSettings.NativeFormat, QtCore.QSettings.UserScope, 'QGIS', 'QGIS2')

settings.beginGroup("Qgis/plugin-repos")
if not 'ARTELIA' in settings.childGroups () :
    print('Artelia not in repos')
    settings.setValue('ARTELIA/autcfg','')
    settings.setValue('ARTELIA/enabled',True)
    settings.setValue('ARTELIA/url',"file://arteliagroup.com/echange_global/FR/ECH/INF_licences/Qgis/plugins.xml")
else:
    print('Artelia in repos')
settings.endGroup()

settings.beginGroup("proxy")
settings.setValue('proxyEnabled',True)
settings.setValue('proxyExcludedUrls','')
settings.setValue('proxyHost','10.1.3.47')
settings.setValue('proxyPassword','')
settings.setValue('proxyPort',3128)
settings.setValue('proxyType','HttpProxy')
settings.setValue('proxyUser','')
settings.endGroup()







print('script finished')
