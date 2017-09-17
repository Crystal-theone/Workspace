class sample:
    def __init__(self,name):
        self.name=name
    def __call__(self,num):
        print(self.name,num)
s=sample("Uzair")
s(1)
s(2)
s(3)