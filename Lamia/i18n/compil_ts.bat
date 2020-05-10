SET OSGEO4W_ROOT=C:\Program Files\OSGeo4W64-310
cd %~dp0

py3_env
qt5_env
pylupdate5 -noobsolete Lamia.pro
pause