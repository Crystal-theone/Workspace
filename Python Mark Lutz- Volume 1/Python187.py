line='aaa bb ccc zz'
res=list(x.upper() for x in line.split(' ') if len(x)==2)
res2=list(map(lambda x:x.upper(),(filter(lambda x:len(x)==2,line.split()))))
print(res)
print(res2)