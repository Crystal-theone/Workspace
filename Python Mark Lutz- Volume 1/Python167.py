def sampleFunction(*sampleArgs):
    min=sampleArgs[0]
    for a in sampleArgs[1:]:
        if a<min:
            min=a
    print(min)
def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first
print(min2(1))
#sampleFunction(*('a','b','c','d','e'))