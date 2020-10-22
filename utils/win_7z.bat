SET LAMIAMETADATA=%~dp0\..\qgisiface\qgispluginroot\metadata.txt

for /f "delims== tokens=1,2" %%G in (%LAMIAMETADATA%) do set %%G=%%H

SET version=%version:.=_%

"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../qgisiface/  ../config/ ../api/

"C:\Program Files\7-Zip\7z" rn Lamia_%version%.zip  qgisiface/qgispluginroot/ Lamia/  ^
                                                    qgisiface/ Lamia/qgisiface/  ^
                                                    config/ Lamia/config/  ^
                                                    api/ Lamia/api/


REM "C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../config/
REM "C:\Program Files\7-Zip\7z" rn Lamia_%version%.zip config/ Lamia/config/ 
REM 
REM "C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../api/
REM "C:\Program Files\7-Zip\7z" rn Lamia_%version%.zip api/ Lamia/api/

cmd /k