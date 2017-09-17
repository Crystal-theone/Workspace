def sampleFunction(a,c,*args,**kargs):
    print a,args,kargs
c=(1,2,3)
d={'b':2,'e':3}
apply(sampleFunction,c,d)
a=1,
print a