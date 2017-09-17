import time
def sampleFunction():
    start=time.clock()
    for i in range(1000):
        pow(i,i)
    end=time.clock()
    total=end-start
    print("Total Time: "+str(total))
sampleFunction()
