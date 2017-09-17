M=[[1,2,3],
   [4,5,6],
   [7,8,9]]
Z=[[11,12,13],
   [14,15,16],
   [17,18,19]]
print(len(M))
M=[[data+10 for data in row] for row in M ]
print(M)
x=[1,2,3]
y=[3,4,5]
r=list(zip(M,Z))
print(r)