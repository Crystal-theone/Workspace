def sampleFunction(data):
    for x in range(data):
        d=yield x
        print(d)
v=sampleFunction(10)
print(v.send(None))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(v.send("Ali"))