def sampleFunctuin():
    def innerFunction():
        nonlocal  sam
        print(sam)
    return innerFunction()
print("Hello")