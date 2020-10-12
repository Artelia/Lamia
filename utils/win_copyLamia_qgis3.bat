rmdir %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia /s /q
mkdir %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia
xcopy %~dp0\..\lamiaqgisiface %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\lamiaqgisiface\  /E /I
xcopy %~dp0\..\lamiaapi %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\lamiaapi\  /E /I
xcopy %~dp0\..\lamiaconf %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\lamiaconf\  /E /I

move %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\lamiaqgisiface\qgispluginroot\*.*  %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia





