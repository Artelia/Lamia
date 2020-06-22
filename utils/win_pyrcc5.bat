SET LAMIADIR=%~dp0\..\Lamia\iface

call %~dp0/win_setqgisenv.bat

cd %OSGEO4W_ROOT%

"%OSGEO4W_ROOT%\apps\Python37\python.exe" -m PyQt5.pyrcc_main "%LAMIADIR%\resources.qrc" -o "%LAMIADIR%\resources_rc.py"

REM cmd /k


