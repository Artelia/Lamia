call %~dp0/win_setqgisenv.bat

REM specific vscode libs/path

path C:\Program Files\Git\cmd;%UserProfile%\AppData\Local\Programs\Git\cmd;%PATH%
path C:\Program Files\Docker\Docker\resources\bin;C:\ProgramData\DockerDesktop\version-bin;%PATH%

REM pip --user for vscode : black, sphinx, sphonx rtd theme
path %UserProfile%\AppData\Roaming\Python\Python37\Scripts;%PATH%
set PYTHONPATH=%UserProfile%\AppData\Roaming\python\Python37\site-packages;%PYTHONPATH%


REM save my life !!!
SET QGIS_DISABLE_MESSAGE_HOOKS=1
SET QGIS_NO_OVERRIDE_IMPORT=1
SET QT_LOGGING_RULES=*.debug=false;*.warning=false

start "PyCharm aware of Quantum GIS" /B "%UserProfile%\AppData\Local\Programs\Microsoft VS Code\Code.exe" %*
