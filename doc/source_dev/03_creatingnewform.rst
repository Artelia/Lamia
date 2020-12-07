.. toctree::
    :maxdepth: 2

Creating a new form
#################################


The minimal form abstracclass
*******************************

A new for class for wowthematic has to be created in Lamia.config.qgswidgets module.
Prefer a name like lamia_form_[table].py
The class is automaticaly loaded when launching lamia.
And you have to create the form qith Qt Designer.


The minimal content is :

.. code-block:: python
    
    from qgis.PyQt.QtWidgets import QWidget
    from qgis.PyQt import uic
    import sys, os
    from Lamia.qgisiface.iface.qgiswidget.tools.lamia_abstractformtool import (
        AbstractLamiaFormTool,
    )

    class BaseTableTool(AbstractLamiaFormTool):
        # the name of the form tool, accessible with lamia API with mainifacewidget.toolwidgets["camera"]
        PREPROTOOLNAME = "camera"  
        # The table the form will interact with     
        DBASETABLENAME = "media"
        # True for "field investigation interface", False for "Desktop interface"
        LOADFIRST = False


        # The name of the root node in the left treewidget of the ui
        tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
        # The name of the sub node in the left treewidget of the ui
        tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Camera")
        # The icon of the sub node in the left treewidget of the ui
        tooltreewidgetICONPATH = os.path.join(
            os.path.dirname(__file__), "lamia_form_camera_icon.svg"
        )


        def __init__(self, **kwargs):
            super(BaseCameraTool, self).__init__(**kwargs)

        def initMainToolWidget(self):
            """
            init the form widget
            """
            # loading the qt widget created with Qt designer
            self.toolwidgetmain = UserUI()
            # the dict defining witch widget within the form qt widget is linked with a field of the table
            # the keys are parent table (linked to main table by a lpk_ field) 
            self.formtoolwidgetconfdictmain = {
                "media": { "widgets": {}},
                "object": {
                    "widgets": {"comment": self.toolwidgetmain.comment,},
                },
                "resource": {
                    "widgets": {
                        "file": self.toolwidgetmain.file,
                        "resourceindex": self.toolwidgetmain.resourceindex,
                        "datetimeresource": self.toolwidgetmain.datetimeresource,
                    },
                },
            }

    class UserUI(QWidget):
        def __init__(self, parent=None):
            super(UserUI, self).__init__(parent=parent)
            uipath = os.path.join(os.path.dirname(__file__), "lamia_form_camera_ui.ui")
            uic.loadUi(uipath, self)



The class variables
***********************

The class variables are :


.. code-block:: python

        # the name of the form tool, accessible with lamia API with mainifacewidget.toolwidgets["camera"]
        PREPROTOOLNAME = "camera"  
        # The table the form will interact with     
        DBASETABLENAME = "media"
        # True for "field investigation interface", False for "Desktop interface"
        LOADFIRST = False


        # The name of the root node in the left treewidget of the ui
        tooltreewidgetCAT = QtCore.QCoreApplication.translate("base3", "Resources")
        # The name of the sub node in the left treewidget of the ui
        tooltreewidgetSUBCAT = QtCore.QCoreApplication.translate("base3", "Camera")
        # The icon of the sub node in the left treewidget of the ui
        tooltreewidgetICONPATH = os.path.join(
            os.path.dirname(__file__), "lamia_form_camera_icon.svg"
        )

        # Used for sub forms : here, if the current form is child of deficiency form (the DBASETABLENAME var), 
        # as a new form is created, it will now to fill the "lid_deficiency" column with the 
        # "id_deficiency" value of parent form
        PARENTJOIN = {
            "deficiency": {
                "colparent": "id_deficiency",
                "colthistable": "lid_deficiency",
                "tctable": None,
                "tctablecolparent": None,
                "tctablecolthistable": None,
            }
        }

        # Show only rows of table with the value set here
        TABLEFILTERFIELD = {"typemedia": "PHO"}

        # var for setting the treewidget at the bottom left of the main ui
        # key colshow : append a table column  to the list of id_resource
        #     sort  : enable sorting ids by the table column 
        CHOOSERTREEWDGSPEC = {
            "colshow": ["datetimeobservation"],
            "sort": ["datetimeobservation", "DESC"],
        }

Inserting child form
***********************

For exemple, we want to have a camera form linked with a particular deficiency. We have to create a subwidget 
in the deficiency form.

It's done in the initMainToolWidget method. We have to :
* create the sub widget
* add it to the var dbasechildwdgfield in the parent form

.. code-block:: python

    def initMainToolWidget(self):
        [...]
        self.dbasechildwdgfield = []
        self.instancekwargs["parentwidget"] = self
        self.propertieswdgOBSERVATION = BaseObservationTool(**self.instancekwargs)
        self.dbasechildwdgfield.append(self.propertieswdgOBSERVATION)


Coding particular behaviours
****************************

Methods inside the form class provide 


.. code-block:: python

    class BaseTableTool(AbstractLamiaFormTool):

        def initMainToolWidget(self):
            """
            Method called on the widget init
            """

        def postSelectFeature(self):
            """
            method called after feature selection
            the var self.currentFeaturePK is None when it's a new feature, and equals the table pk when 
            it's an existing feature
            """
            if self.currentFeaturePK is None:
                [...]
            else:
                [...]

        def postSaveFeature(self, savedfeaturepk=None):
            """
            method called when feature is saved
            savedfeaturepk : the pk af the saved feature
            """
            [...]

        def magicFunction(self):
            """
            method called when click on magic icon
            """
            [...]