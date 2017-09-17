from __future__ import division
from math import sqrt as SQR
from functools import reduce
#Simple keywords arguments code
def adder(**kwargs):
    sum=0 if type(kwargs[list(kwargs.keys())[0]])==int else kwargs[list(kwargs.keys())[0]][:0]
    for k in kwargs.keys():
        sum+=kwargs[k]
    return sum
#Copy dictionary code
def copyDictionary(dictionary):
    default={}
    for keys in dict(dictionary).keys():
        default[keys]=dictionary[keys][:]
    return default
#Union code for dictionary
def addDictionary(dict1,dict2):
    resultantDictionary=dict1
    iterable=list(dict(dict2).keys()) if dict2 is dict else dict2
    dic=True if dict2 is dict else False
    for key in iterable:
        if dic:
            if not key in dict(resultantDictionary).keys():
                resultantDictionary[key]=dict(dict2)[key];
        else:
            if not key in resultantDictionary:
                resultantDictionary.append(key)
    return resultantDictionary
#Prime number code
def primeNumberChecker(y):
    x=y//2
    while x>1:
        if y%x==0:
            print(y,' has a factor ',x)
            break;
        x-=1
    else:
        print(y,' is a prime number')
#Comprehension and Iteration
def doListComprehension(data):
    return [SQR(d)for d in data]

def doItertation(data):
    result=[]
    for d in data:
        result.append(SQR(d))
    return result

def doMapping(data):
    return list(map(SQR,data))

def doGeneration(data):
    return list(SQR(x)for x in data)
#Recursive functions
def countDown(value):
    if value==0:
        print("Stop")
        return
    print(value)
    return countDown(value-1)
#Factorial Functions
def recursiveFactorial(value):
    if value==0:
        return 1
    return value*recursiveFactorial(value-1)
def reduceFactorial(value):
    return reduce(lambda x,y:x*y,list(range(value,1,-1)))
def iterativeFactorial(value):
    result=1 if value<=0 else value
    for i in range(value-1,1,-1):
        result *= i
    return result
def functionalFactorial(value):
    from math import factorial
    return factorial(value)