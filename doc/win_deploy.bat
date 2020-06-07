SET OSGEO4W_ROOT=C:\OSGeo4W64

cd %OSGEO4W_ROOT%
@echo off
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
@echo on
call py3_env.bat
call qt5_env.bat
@echo on

del /Q %~dp0\build\html

REM call  "%CD%\makehtml.bat"

cd %~dp0
call make html

REM @echo Start copy to Lamia\doc_html ...
REM xcopy /E /Y /S /I /Q %~dp0\build\html %~dp0\..\Lamia\doc_html
REM @echo Finish copy to Lamia\doc_html

REM cmd /k







