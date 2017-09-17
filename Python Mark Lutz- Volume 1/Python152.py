def sampleFunction():
    act=[]
    for i in range(5):
        act.append(lambda x:i**x)
    return act
s=sampleFunction()
print(s[1](2))