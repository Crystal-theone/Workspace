def sample(start):
    def innerSample(final):
        print(final,innerSample.state)
        innerSample.state+=1
    innerSample.state=start
    return  innerSample
s=sample(22)
s("Wow")
