def sampleFunction(a,b=2,c=3):
    print(a,b,c)
def sampleDefaults(a=[]):
    a.append(1);
    print(a,id(a))
#sampleFunction(b=3,c=33,a=22)
sampleDefaults()
sampleDefaults()