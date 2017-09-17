def sampleScope(x):
    def sampleInnerScope(z):
        return x+z
    return sampleInnerScope
sample=sampleScope(2)
print(sample(2))
print(sample(3))
print(sample(4))