def sampleFunction():
    x=22
    def sampleInnerFunction():
        print (x+2)
    def sampleInnerFunction2():
        print(x+4)
    sampleInnerFunction()
    sampleInnerFunction2()
sampleFunction()