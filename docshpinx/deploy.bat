SET OSGEO4W_ROOT=C:\Program Files\OSGeo4W64-310

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

@echo Start copy to Lamia\doc_html ...
xcopy /E /Y /S /I /Q %~dp0\build\html %~dp0\..\Lamia\doc_html
@echo Finish copy to Lamia\doc_html

cmd /k







