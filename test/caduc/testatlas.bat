@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W64
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
call "%OSGEO4W_ROOT%"\apps\grass\grass-7.2.1\etc\env.bat

@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass-7.2.1\lib

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
REM set PYTHONPATH=%PYTHONPATH%;C:\Users\patrice.verchere\.qgis2\python\plugins
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
REM set PATH=C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.2\bin\pycharm.exe;%PATH%
REM cd %HOMEPATH%\development



REM start "PyCharm aware of Quantum GIS" /B "C:\Program Files\JetBrains\PyCharm Community Edition 2017.2.3\bin\pycharm.exe" %*
python testatlas.py