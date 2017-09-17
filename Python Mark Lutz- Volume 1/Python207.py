x=100
def sampleFunction():
    import __main__
    print(__main__.x)
    x=999
    print(x)
sampleFunction()