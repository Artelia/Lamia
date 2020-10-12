SET LAMIAMETADATA=%~dp0\..\lamiaqgisiface\qgispluginroot\metadata.txt

for /f "delims== tokens=1,2" %%G in (%LAMIAMETADATA%) do set %%G=%%H

SET version=%version:.=_%

"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../lamiaqgisiface/
"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../lamiaconf/
"C:\Program Files\7-Zip\7z" a -xr!__pycache__ Lamia_%version%.zip ../lamiaapi/

"C:\Program Files\7-Zip\7z" rn Lamia_%version%.zip  lamiaqgisiface/qgispluginroot/ lamia/  ^
                                                    lamiaqgisiface/ lamia/lamiaqgisiface/  ^
                                                    lamiaconf/ lamia/lamiaconf/  ^
                                                    lamiaapi/ lamia/lamiaapi/