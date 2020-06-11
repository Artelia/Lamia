call %~dp0/../win_setqgisenv.bat
cd %~dp0

SET DESTINATIONDIR="C:\01_WORKINGDIR\GPMB\c_merge_aep"

REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\BACALAN\GPMB Bacalan.sqlite"
REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\BASSENS\EU\Bassens EU EP.sqlite"
REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\BLAYE\GPMB Blaye.sqlite"
REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\Pauillac\GPMB Pauillac.sqlite"
REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\POLE NAVAL\EU\Pole naval.sqlite"
REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\Verdon port bloc\GPMB Port Bloc.sqlite"
REM set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\Verdon Terminal conteneur\GPMB Verdon Terminal conteneur.sqlite"

set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\POLE NAVAL\AEP\Pole Naval_AEP.sqlite"
set MERGEFILE=%MERGEFILE%;"C:\01_WORKINGDIR\GPMB\b_result\BASSENS\AEP\Bassens-AEP.sqlite"


"%OSGEO4W_ROOT%\apps\Python37\python.exe"  pymerger.py %DESTINATIONDIR% %MERGEFILE%