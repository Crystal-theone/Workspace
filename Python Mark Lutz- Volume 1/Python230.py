class Person(object):
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def __get__(self, instance, owner):
        print "Accessing the Get Property"
        return self.firstName+" "+self.lastName
    def __set__(self, instance, value):
        print "Accessing the Set Property"
        self.firstName=value
class ClassRoom(object):
    a=Person("Uzair","Tariq")

    def __getattribute__(self, item):
        print "Attribute was tried to be accessed "+item
        return super(ClassRoom,self).__getattribute__(item);
    def __getattr__(self, item):
        print item+" not found"

c=ClassRoom()
print c.a