SET OSGEO4W_ROOT=C:\Program Files\OSGeo4W64-310
@echo off
cd %OSGEO4W_ROOT%
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
call py3_env.bat
call qt5_env.bat
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python37\lib\site-packages
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
cd %~dp0
@echo on