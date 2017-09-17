class Uzair:
    x=1
    def name(self,name):
        self.named=name;
        print "My name is"+name

print Uzair.__dict__
a=Uzair()
a.x=2
print a.__dict__
print Uzair.__dict__