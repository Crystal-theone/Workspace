list=[[1,2,3],
      [4,[1,2,3],6]]
print(list)
print("Extracting List")
column=[row[1] for row in list]
print(column)