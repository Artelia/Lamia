call %~dp0/../win_setqgisenv.bat
cd %~dp0

path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass78\lib
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin
SET QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins

python -m cProfile -o profileresult.cprof 00_launchqtiface.py