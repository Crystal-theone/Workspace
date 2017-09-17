res=[]
d=list(map(lambda x:(tuple(map(lambda y:res.append((x,y)),filter(lambda y:y%2!=0,range(5))))),filter(lambda x:x%2==0,range(5))))
print(res)