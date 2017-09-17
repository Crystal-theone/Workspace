class Worker:
    uzi="Ali";
    def __init__(self,name,salary):
        self.name=name;
        self.salary=salary;
    def getLastName(self):
        return self.name.split()[-1];
    def giveRaise(self,ammount):
        self.salary*=(1.0+ammount);
    def changeName(self,updatedName):
        self.uzi=updatedName;
        print("Values Updated");