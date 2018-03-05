import os
import glob, importlib, inspect


path = os.path.join(os.path.dirname(__file__), '..', 'toolprepro')
modules = glob.glob(path + "/*.py")
__all__ = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
for x in __all__:
    #print(x)

    if True:
        moduletemp = importlib.import_module('.' + str(x), 'Lamia.Lamia.toolprepro')
        # print(moduletemp)
        # print(moduletemp.TEST)
        for name, obj in inspect.getmembers(moduletemp, inspect.isclass):
            #print(name,obj,obj.__module__, moduletemp.__name__)
            if moduletemp.__name__ == obj.__module__:
                try:
                    if obj.LOADFIRST:
                        print(x, name, obj)
                        print(obj.TEST2)
                    else:
                        print(x, name, obj)
                        print(obj.TEST2)
                except AttributeError:
                    pass

