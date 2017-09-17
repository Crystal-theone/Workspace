import sys,Modules.Timer as Tim
reps=1000
repsList=list(range(reps))
def forloop():
    res = []
    for i in repsList:
        res.append(abs(i))
    return res
def listComprehension():
    return [abs(x) for x in repsList]
def mapCall():
    return list(map(abs,repsList))
def genrator():
    return list(abs(x) for x in repsList)
def genratorFunction():
    def gen():
        for i in repsList:
            yield abs(i)
    return list(gen())
print(sys.version)
for test in (forloop,listComprehension,mapCall,genrator,genratorFunction):
    (bestof,(total,result))=Tim.bestoftotal(5,1000,test)
    print((bestof,(total,result)))
    print('%-9s:%.5f => [%s...%s]'%(test.__name__,bestof,result[0],result[-1]))
