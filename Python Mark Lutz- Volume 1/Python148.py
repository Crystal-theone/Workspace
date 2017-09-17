data=99
def mod1():
    data=0
    print(data)
def mod2():
    global data
    data+=1
    print(data)
def mod3():
    var=0
    print(var)
    import Python148
    Python148.data+=1
    print(data)
def mod4():
    var = 0
    print(var)
    import sys
    glob=sys.modules['Python148']
    glob.data+=88
    print(data)
def test():
    mod1()
    mod2()
    mod3()
    mod4()