call %~dp0/../win_setqgisenv.bat
cd %~dp0

SET LAMIADIR="POLE NAVAL\AEP\Pole Naval_AEP.sqlite"
REM Base2_eaupotable_base2_0_4_to_base3_0_1.ods Base_assainissement_base2_0_6_to_base3_0_1.ods
SET ODSFILES="Base2_0_8to3_0_1.ods Base2_eaupotable_base2_0_4_to_base3_0_1.ods"

"%OSGEO4W_ROOT%\apps\Python37\python.exe"  converterbase2_base3.py %LAMIADIR% %ODSFILES%
