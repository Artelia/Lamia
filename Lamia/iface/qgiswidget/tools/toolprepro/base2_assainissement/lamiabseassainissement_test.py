from ...lamia_abstractformtool import AbstractLamiaFormTool
import os
import datetime



class BaseAssainissementTestTool(AbstractLamiaFormTool):

    DBASETABLENAME = 'Infralineaire'
    LOADFIRST = True

    tooltreewidgetCAT = 'abba'
    tooltreewidgetSUBCAT = 'Test'

    def __init__(self,**kwargs):
        super(BaseAssainissementTestTool, self).__init__(**kwargs)