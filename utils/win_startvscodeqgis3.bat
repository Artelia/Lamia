@echo off
SET OSGEO4W_ROOT=C:\Program Files\OSGeo4W64-310
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
call "%OSGEO4W_ROOT%"\apps\grass\grass78\etc\env.bat

@echo off
path %PATH%;C:\Program Files\Git\cmd;C:\Program Files\Docker\Docker\resources\bin;C:\Users\patrice.verchere\AppData\Local\Programs\Git\cmd;C:\ProgramData\DockerDesktop\version-bin
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass78\lib
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin
REM path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms\qwindows.dll
REM path %PATH%;%OSGEO4W_ROOT%\apps\Python37\Scripts

REM set PYTHONPATH=%OSGEO4W_ROOT%\apps\Python36
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python37\lib\site-packages
REM set PYTHONPATH=%PYTHONPATH%;C:\Users\patrice.verchere\.qgis2\python\plugins
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis

SET QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins


REM save my life !!!
SET QGIS_DISABLE_MESSAGE_HOOKS=1
SET QGIS_NO_OVERRIDE_IMPORT=1
SET QT_LOGGING_RULES=*.debug=false;*.warning=false


set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37

REM set PATH=C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.5\bin\pycharm.exe;%PATH%
REM cd %HOMEPATH%\development



start "PyCharm aware of Quantum GIS" /B "C:\Users\patrice.verchere\AppData\Local\Programs\Microsoft VS Code\Code.exe" %*