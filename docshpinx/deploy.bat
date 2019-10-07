del /Q %~dp0\source\images
del %~dp0\source\*.rst

python %~dp0\odt2sphinx\odt2sphinx.py documentation.odt %~dp0\source
REM odt2sphinx documentation.odt %~dp0\source

del /Q %~dp0\build\html

call  makehtml.bat

@echo Start copy to Lamia\doc_html ...
xcopy /E /Y /S /I /Q %~dp0\build\html %~dp0\..\Lamia\doc_html
@echo Finish copy to Lamia\doc_html







