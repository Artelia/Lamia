REM SET OSGEO4W_ROOT=C:\OSGeo4W64
SET OSGEO4W_ROOT=C:\Program Files\OSGeo4W64-310

cd %OSGEO4W_ROOT%
@echo off
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
@echo on
call py3_env.bat
call qt5_env.bat
@echo on

del  /Q /S %~dp0\build\


cd %~dp0
call make_fr html
call make_en html
call make_dev html

REM @echo Start copy to Lamia\doc_html ...
REM xcopy /E /Y /S /I /Q %~dp0\build\html %~dp0\..\Lamia\doc_html
REM @echo Finish copy to Lamia\doc_html

REM cmd /k







