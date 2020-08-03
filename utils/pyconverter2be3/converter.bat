call %~dp0/../win_setqgisenv.bat
cd %~dp0

SET SOURCEFILE="C:\01_WORKINGDIR\lamia\from\CC_Bastides_Dordogne_Perigord-B.sqlite"
REM ***** ASS ***********
REM \BACALAN\GPMB Bacalan.sqlite       BASSENS\EU\Bassens EU EP.sqlite  BLAYE\GPMB Blaye.sqlite
REM Pauillac\GPMB Pauillac.sqlite   POLE NAVAL\EU\Pole naval.sqlite Verdon port bloc\GPMB Port Bloc.sqlite
REM Verdon Terminal conteneur\GPMB Verdon Terminal conteneur.sqlite
REM ***** AEP ***********
REM POLE NAVAL\AEP\Pole Naval_AEP.sqlite    BASSENS\AEP\Bassens-AEP.sqlite

 
SET DESTDIR="C:\01_WORKINGDIR\lamia\to"
REM Base2_eaupotable_base2_0_4_to_base3_0_1.ods Base_assainissement_base2_0_6_to_base3_0_1.ods
REM base_digue_base2_0_5_base3_0_1
SET ODSFILES="Base2_0_8to3_0_1.ods Base_assainissement_base2_0_6_to_base3_0_1.ods"


"%OSGEO4W_ROOT%\apps\Python37\python.exe"  converterbase2_base3.py %SOURCEFILE% %DESTDIR% %ODSFILES%
