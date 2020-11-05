import qgis, qgis.core, qgis.gui, qgis.utils
import sys, os

sys.path.append(r"C:\OSGeo4W64\apps\qgis\python")

lamiapath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(lamiapath)
import pyplugin_installer

qgis.utils.home_plugin_path = r"C:\Users\patrice.verchere\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins"

pyplugin_installer.instance().installFromZipFile(
    r"C:\111_GitProjects\Lamia\utils\Lamia_1_016.zip"
)

# import Lamia

print(qgis.utils.loadPlugin("Lamia"))

print(qgis.utils.available_plugins)
