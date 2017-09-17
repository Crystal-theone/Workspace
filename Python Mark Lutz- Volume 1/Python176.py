def sampleFunction(familyName):
    def getName(childName):
        sampleFunction.family=familyName;
        print(sampleFunction.family+" "+childName);
    return getName;
completeName=sampleFunction("Senuch")
completeName("Ibrahim");
completeName("Ismail");
completeName2=sampleFunction("Tariq")
completeName2("Uzair")

