dictionaty={
    "alredy":lambda :2+2,"got":lambda :2*2,"one":lambda :2**2,"sample":lambda *args:print(args)
}
#print(dictionaty["sample"](1,2,3,4,5))
s=(lambda x:lambda y:(x+y))
f=s(10)
print(f(1))

