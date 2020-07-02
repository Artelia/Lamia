SET QGISDATA=%~dp0\qgisconfig.txt
for /f "delims== tokens=1,2" %%G in (%QGISDATA%) do set %%G=%%H

SET OSGEO4W_ROOT=%OSGEOPATH%
SET QGISPATH=%QGISPATH%

@echo off
cd %OSGEO4W_ROOT%
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
call py3_env.bat
call qt5_env.bat
path %QGISPATH%\bin;%PATH%
REM path %UserProfile%\AppData\Roaming\Python\Python37\Scripts;%PATH%
set QGIS_PREFIX_PATH=%QGISPATH%
set QT_PLUGIN_PATH=%QGISPATH%\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
set PYTHONPATH=%QGISPATH%\python;%PYTHONPATH%
REM set PYTHONPATH=%UserProfile%\AppData\Roaming\python\Python37\site-packages;%PYTHONPATH%

REM set PYTHONPATH=%PYTHONPATH%;%QGISPATH%\python;
REM set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python37\lib\site-packages
REM set QGIS_PREFIX_PATH=%QGISPATH%

REM Display env with powershell : Get-ChildItem Env:

cd %~dp0
@echo on
