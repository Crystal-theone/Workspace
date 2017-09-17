d1=["a","b","c","d","e"];
d2=[1,2,3,4,5,6];
dic=dict(zip(d1,d2));
print(dic)
r1=[x*2 for x in d2];
print(r1)
dic2={k:v for(k,v) in zip(d1,d2)}
print(dic2)
