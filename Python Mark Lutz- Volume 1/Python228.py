from Python227 import FirstClass
class SecondClass(FirstClass):
    def displayData(self):
        print "Okay I am the data from the secondary class "+self.data

class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value;
    def __add__(self, other):
        return ThirdClass(self.data+other)
    def __str__(self):
        return '[Third Class %s]'%self.data
    def mul(self,other):
        self.data*=other
if __name__=='__main__':
    one = SecondClass()
    one.setData("Uzair")