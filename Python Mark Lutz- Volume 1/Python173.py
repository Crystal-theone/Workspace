def customSum(values):
    if not values:
        return 0
    else:
        return values[0]+customSum(values[1:])
print(customSum([1,2,3,4]))