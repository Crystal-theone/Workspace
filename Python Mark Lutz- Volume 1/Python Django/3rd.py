cost1=10
cost2=20
cost3=30
cost4=40
def sumCart(item1,item2=2):
    totalCost=item1+item2
    print totalCost
def sumCart2(item1,item2=2):
    totalCost=item1+item2
    return totalCost
sumCart(cost1,cost2)
sumCart(cost1)
answer1=sumCart2(cost3)
answer2=sumCart2(cost3,cost1)
print answer1+answer2