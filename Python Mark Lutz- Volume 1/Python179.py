def sampleFunction(x):
    return x+10;
iterable=(1,2,3,4,5,6)
res=map(sampleFunction,iterable)
print(list(res))