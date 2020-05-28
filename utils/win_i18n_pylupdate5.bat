SET OSGEO4W_ROOT=C:\Program Files\OSGeo4W64-310
SET LAMIADIR=%~dp0\..\Lamia\i18n


echo %LAMIADIR%
cd %OSGEO4W_ROOT%
@echo off
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
@echo on
call py3_env.bat

call qt5_env.bat
@echo on
REM PAUSE
REM call pylupdate5 -noobsolete Lamia.pro

"%OSGEO4W_ROOT%\apps\Python37\python.exe"  -m PyQt5.pylupdate_main -noobsolete -verbose %LAMIADIR%\Lamia.pro


cmd /k


