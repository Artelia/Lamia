SET LAMIAMETADATA=%~dp0\..\qgisiface\qgispluginroot\metadata.txt

for /f "delims== tokens=1,2" %%G in (%LAMIAMETADATA%) do set %%G=%%H

SET version=%version:.=_%

"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../qgisiface/
"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../config/
"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../api/

"C:\Program Files\7-Zip\7z" rn Lamia_%version%.zip  qgisiface/qgispluginroot/ lamia/  ^
                                                    qgisiface/ lamia/qgisiface/  ^
                                                    config/ lamia/config/  ^
                                                    api/ lamia/api/