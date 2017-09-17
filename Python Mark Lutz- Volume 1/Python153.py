def sampleFunction():
    act=[]
    for i in range(10):
        act.append(lambda x,i=i:x**i)
    return act
s=sampleFunction()
for i in range(len(s)):
    print(s[i](i))