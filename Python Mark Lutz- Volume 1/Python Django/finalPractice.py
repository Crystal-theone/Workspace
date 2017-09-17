class Animals:
    number_of_legs=0
    def sleep(self):
        print "Zzzz!"
    def countLegs(self):
        print "I have %s legs"%self.number_of_legs

class Dog(Animals):
    def bark(self):
        print "Wofff"

dog=Dog()
dog.bark()
dog.sleep()
dog.number_of_legs=4
dog.countLegs()
