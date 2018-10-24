# -*- coding: utf-8 -*-

if False:
    a = 'oioié'
    print(a)
    print(type(a))

    import os
    import qgis
    import sys

    print(sys.version_info.major)

    sys.tracebacklimit = 0


    print(os.environ.get('QGIS_DISABLE_MESSAGE_HOOKS'))
    print(sys.stdout)
    print(sys.excepthook)

    # sys.tracebacklimit = 0



    import qgis.gui




    import qgis.utils

    print(sys.stdout)
    print(sys.excepthook)

    if False:
        def exception_handler(exception_type, exception, traceback):
            # All your trace are belong to us!
            # your format
            print("%s: %s" % (exception_type.__name__, exception))

        sys.excepthook = exception_handler


    print(qgis.utils.iface)

    a.decode('utf-8')


if False:
    import qgis

    import qgis.utils

    # qgis.utils.uninstallErrorHook()

    print(qgis.utils.iface)

    print(b'popo'.decode('utf-8'))
    print(str('popo').decode('utf-8'))


if True:
    import inspect, glob, importlib, os

    uifields = []
    uidesktop = []

    path = os.path.join(os.path.dirname(__file__), '..', 'toolprepro', 'digue')
    modules = glob.glob(path + "/*.py")
    __all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]

    import Lamia

    for x in __all__:

        if False:
            #   if not self.dbase.standalone:
            moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + 'digue')
            # moduletemp = importlib.import_module('.' + str(x), 'Lamia.toolprepro.' + self.dbase.type.lower())
            # moduletemp = importlib.import_module('.' + str(x), '..toolprepro.' + self.dbase.type.lower())
        else:
            moduletemp = importlib.import_module('.' + str(x), 'Lamia.Lamia.toolprepro.' + 'digue')


        for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
            if moduletemp.__name__ == obj.__module__:
                try:
                    if obj.LOADFIRST:
                        uifields.append(obj)
                    else:
                        uidesktop.append(obj)
                except AttributeError:
                    pass



print('ok')