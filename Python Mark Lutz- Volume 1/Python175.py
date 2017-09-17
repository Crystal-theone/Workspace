def sampleFunction(L):
    total=0
    data=list(L)
    while data:
        print(data)
        front=data.pop(0)
        if  not isinstance(front,list):
            total+=front
        else:
            data.extend(front)
    return total
def sampleFunction2(L):
    total=0
    data=list(L)
    while data:
        front=data.pop(0)
        if not isinstance(front,list):
            total+=front
        else:
            data[:0]=front
    return total
L=[1,[99,99],3,[1,2,3,[3,3,3]]]
#print(sampleFunction2(L))
#print(sampleFunction(L))
