def sampleRecursion(L):
    total=0
    for x in L:
        if  not isinstance(x,list):
            total+=x
        else:
            total+=sampleRecursion(x)
    return total
l=[1,2,[1,[2,3],4],[5,[5,[6,7,8]]]]
print(sampleRecursion(l))
