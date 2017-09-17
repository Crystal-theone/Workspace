def sampleFunction(value):
    def calculation(multiplier):
        return multiplier**value
    return  calculation
f=sampleFunction(2)
print(f(2))