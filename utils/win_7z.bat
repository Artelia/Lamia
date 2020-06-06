SET LAMIAMETADATA=%~dp0\..\Lamia\metadata.txt
for /f "delims== tokens=1,2" %%G in (%LAMIAMETADATA%) do set %%G=%%H

SET version=%version:.=_%

"C:\Program Files\7-Zip\7z" a -xr!__pycache__ lamia_%version%.zip ../Lamia/