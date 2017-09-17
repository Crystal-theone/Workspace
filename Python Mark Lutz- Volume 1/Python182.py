def square(x):
    for i in range(x):
        yield i**2;
x=square(10)
i1=iter(x)
i2=iter(x)
print(next(i1))
print(next(i2))
print(next(i1))
print(next(i2))