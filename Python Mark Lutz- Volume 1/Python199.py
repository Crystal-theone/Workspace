def myzip(*args):
    iters = list(map(iter, args))
    for i in range(3):
        res = [next(i) for i in iters]
        yield tuple(res)
    res2 = [next(i) for i in iters]
    yield tuple(res2)
def check(data):
    return True if data else False
a=myzip("asd","zsd")
print(next(a))
print(next(a))
print(next(a))
#print(list(a))