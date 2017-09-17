B='1101'
i=0;
while B!='':
    i=i*2+(ord(B[0])-ord('0'))
    B=B[1:]
    print(B+" "+str(i))
print("Final B"+repr(B))
