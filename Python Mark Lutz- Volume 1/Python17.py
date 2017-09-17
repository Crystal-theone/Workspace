list=[[1,2,3],
      [4,5,6],
      [7,8,9]]
print("Column Before Processing")
print([row[1] for row in list])
print("Column after Processing")
print([row[1]for row in list if row[1]%2==0])