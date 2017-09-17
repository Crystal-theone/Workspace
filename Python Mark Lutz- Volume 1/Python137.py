d=[1,2,4,8,16,33,64,128,256,512]
i=0
while i<len(d):
    if d[i]==(2**5):
        print("Value found at index %d"%i)
        break
    i+=1
else:
    print("Value not found.")