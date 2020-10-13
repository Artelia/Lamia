SET LAMIADIR=%~dp0\..\qgisiface\i18n


call %~dp0/win_setqgisenv.bat
cd %~dp0

"%OSGEO4W_ROOT%\apps\Python37\python.exe"  -m PyQt5.pylupdate_main -noobsolete -verbose %LAMIADIR%\Lamia.pro


cmd /k


