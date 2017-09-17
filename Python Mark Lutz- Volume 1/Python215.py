import types
from imp import reload
def status(module):
    print "Module name"+module.__name__

def try_reload(module):
    try:
        reload(module)
    except:
        print "Reload Failed %s"%module

def transitive_reload(args,visited):
    if not args in visited:
        status(args)
        try_reload(args)
        visited[args]=True
        for attributes in args.__dict__.values():
            if type(attributes)==types.ModuleType:
                transitive_reload(attributes,visited)


def reload_all(*args):
    visited={}
    for arg in args:
        if type(arg)==types.ModuleType:
            transitive_reload(arg,visited)


def tester(reloader,modname):
    import importlib,sys
    if len(sys.argv)>1:modname=sys.argv[1];
    modname=importlib.import_module(modname)
    reloader(modname)

if __name__=="__main__":
    tester(reload_all,"Python215")