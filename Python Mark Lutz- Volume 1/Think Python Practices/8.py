def do_n(funObj,n):
    if n<=0:
        return
    funObj()
    do_n(funObj,n-1)
def sampleFunction():
    print "Okay i am a sample function."
do_n(sampleFunction,3)
