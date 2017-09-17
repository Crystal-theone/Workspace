data=[1,2,3,4,5]
def getTotalCost(listData):
    totalCost=0
    for d in listData:
        totalCost+=d
    return totalCost
print getTotalCost(data)