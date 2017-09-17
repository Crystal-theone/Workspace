list=[[1,2,3],
      [4,5,6],
      [7,8,9]]
print("Before Processing Row")
column=[row[1] for row in list]
print(column)
print("After Processing Row")
column=[row[1]+1 for row in list]
print((column))