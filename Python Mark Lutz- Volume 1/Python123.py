data=[1,2,3,4,5];
i=0;
for x in data:
    x+=1;
    if(x is data[i]):
        print("Yes")
        x+=1;
    else:
        print("No");
    i+=1;
print(data);