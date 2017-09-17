import types
from imp import reload
def reloader(module,reloadedModules):
    if not module in reloadedModules:
        reload(module)
        reloadedModules.add(module)
        for obj in module.__dict__.values():
            if type(obj) is types.ModuleType:
                reloader(obj,reloadedModules)

def reloadManager(moduleName):
    import importlib
    if not moduleName:return
    module=importlib.import_module(moduleName)
    datas=set()
    reloader(module,datas)