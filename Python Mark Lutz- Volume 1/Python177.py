def sampleFunction(a:"Arguement 1",b:"Argument 2"=2)->"Okay I am Return Type":
    print(a+b)
sampleFunction(b=2,a=2)
print(sampleFunction.__annotations__)