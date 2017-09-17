def sample1():
    for d in sample2():
        print(d)
    yield 1
    yield 2
def sample2():
    yield 4
    yield 5
print(next(sample1()))
