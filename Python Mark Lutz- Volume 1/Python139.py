data=[1,2,4,8,16,33,64,128,256,512]
if (2**8) in data:
    print("Value found at index::"+str(data.index(2**8)))
else:
    print("Value not found.")