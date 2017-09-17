from Modules.PartVI import*
import timeit
#a={'a':'1','b':'2','c':'3'}
#b={'c':4,'d':'4','e':'5','f':'6','g':'7','h':'8','i':'9'}
#c=[1,2,3,4,5,6]
#d=[6,7,8,9]
#print(addDictionary(c,d))
#Prime number check
#primeNumberChecker(3.0)
#data=[2,4,9,16,25]
#print(doListComprehension(data))
#print(doItertation(data))
#print(doMapping(data))
#print(doGeneration(data))
#countDown(5)
print("Function Factorial ",functionalFactorial(50))
print(min(timeit.repeat(stmt="functionalFactorial(50)",setup='from Modules.PartVI import functionalFactorial',repeat=5,number=1000)))
print("Recursive Factorial ",recursiveFactorial(50))
print(min(timeit.repeat(stmt="recursiveFactorial(50)",setup='from Modules.PartVI import recursiveFactorial',repeat=5,number=1000)))
print("Iterative Factorial ",iterativeFactorial(50))
print(min(timeit.repeat(stmt="iterativeFactorial(50)",setup='from Modules.PartVI import iterativeFactorial',repeat=5,number=1000)))
print("Reduce Factorial ",reduceFactorial(50))
print(min(timeit.repeat(stmt="reduceFactorial(50)",setup='from Modules.PartVI import reduceFactorial',repeat=5,number=1000)))