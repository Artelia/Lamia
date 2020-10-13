rmdir %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia /s /q
mkdir %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia
xcopy %~dp0\..\qgisiface %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\qgisiface\  /E /I
xcopy %~dp0\..\api %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\api\  /E /I
xcopy %~dp0\..\config %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\config\  /E /I

move %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\qgisiface\qgispluginroot\*.*  %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia





