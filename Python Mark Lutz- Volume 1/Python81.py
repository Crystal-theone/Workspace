someList=list('Spam');
print(someList);
str="I am a first word {0[0]}".format(someList);
print(str)
str="I am a first word {1[0]} and I am second {1[1]}".format(someList[0],someList);
print(str)