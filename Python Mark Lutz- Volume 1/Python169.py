def myCustomIntersection(*args):
    res=[]
    tuple=args[0]
    for x in tuple:
        exist=True
        for t in args[1:]:
            if (x not in t):
                exist=False
        if exist:
            res.append(x)
    return res
def sampleCheck():
    for x in range(10):
        for y in range(12):
            if y>=7:break
            else:print(y,end=' ')
def mybookReadFunction(*args):
    res=[]
    for x in args[0]:
        if x in res:continue
        for t in args[1:]:
            if x not in t:break
        else:
            res.append(x)
    return res
def sample2(*items):
    print(items)
elements=((1,2,3),(3,2,1),(4,5,6))
sample2(*elements)