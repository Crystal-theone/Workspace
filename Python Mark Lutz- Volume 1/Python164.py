def sampleFunction(*args):
    print(args)
def sampleFunction2(**arg):
    for key,value in arg.items():
        print(arg[key],value)
sampleFunction(1,2,3,4,5)
sampleFunction2(name="Uzair",father="tariq")
d={'name':'uzair','father':'tariq'}
print(d)