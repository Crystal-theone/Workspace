B='1101'
i=0;
power=0;
while B!='':
    i+=int(B[len(B)-1])*(2**power);
    B=B[:-1]
    power+=1
print(i)
