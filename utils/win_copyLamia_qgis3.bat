rmdir %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia /s /q
mkdir %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia
xcopy %~dp0\..\Lamia %UserProfile%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Lamia\ /s /E /EXCLUDE:%~dp0\copylamia_exclude.txt





