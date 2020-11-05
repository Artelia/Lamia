call %~dp0/win_setqgisenv.bat
cd %~dp0

"%OSGEO4W_ROOT%\apps\Python37\python.exe"  zipthis.py

cmd /k