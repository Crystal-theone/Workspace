list=[[1,2,3],
      [4,5,6]]
print(list)
sums=(sum(s) for s in list)
list=[next(sums),next(sums)]
print(list)