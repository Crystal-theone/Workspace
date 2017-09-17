data=[1,2,4,8,16,33,64,128,256,512]
for d in data:
    if d==2**5:
        index=data.index(d)
        print("Index of value is "+str(index))
        break
else:
    print("Value not present in the list.")