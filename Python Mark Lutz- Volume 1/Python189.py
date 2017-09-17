def sampleFunction(N):
    for i in range(N):
        yield i;
    for i2 in range(N*2):
        yield "Called";
result=sampleFunction(3)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))