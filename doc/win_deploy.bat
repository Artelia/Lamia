call %~dp0/../utils/win_setqgisenv.bat

del  /Q /S %~dp0\build\


cd %~dp0
call make_fr html
call make_en html
call make_dev html

REM @echo Start copy to Lamia\doc_html ...
REM xcopy /E /Y /S /I /Q %~dp0\build\html %~dp0\..\Lamia\doc_html
REM @echo Finish copy to Lamia\doc_html

REM cmd /k







