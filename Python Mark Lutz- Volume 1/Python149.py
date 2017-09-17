x=99
def sampleFunction():
    global x
    x=22
    def localFunction():
        x=33
        print(x)
        def localFunction2():
            print (x+2)
        localFunction2()
    localFunction()
sampleFunction()
print(x)