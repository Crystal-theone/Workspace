x=1
def samplelocalScope():
    y=2
    def samplelocalScope2():
        z=3
        nonlocal y
        y=6
        print (x,y,z)
    samplelocalScope2()
    print(y)


samplelocalScope()
