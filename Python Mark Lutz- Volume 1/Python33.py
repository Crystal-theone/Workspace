dictionary={'a':1,'b':2,'c':3,'d':4}
print("Dictionary data before processing")
print(dictionary)
localList=list(dictionary.keys())
print("List of present key::"+str(localList))
print("List of keys after sortion::"+str(localList.sort()))
for keys in localList:
    print(keys+"=>"+str(dictionary[keys]))