def arbFunction(fun,a,*pargs,**kargs):
    print(fun.__name__)
    fun(a,*pargs,**kargs)
def sampleFunction(*parg,**kargs):
    t=sum(parg)+sum(kargs.values())
    print(t)
arbFunction(sampleFunction,1,2,3,z=4,c=5)