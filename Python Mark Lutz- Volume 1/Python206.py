import timeit
def fun(x):
    return x+1
s1=timeit.repeat(setup="def fun(x):\n\treturn x+1",stmt="fun(1)",number=1000,repeat=5)[0]
s2=timeit.repeat(setup="def fun(x):\n\treturn x+1",stmt="list(map(fun,[1]))",number=1000,repeat=5)[0]
print(s1)
print(s2)