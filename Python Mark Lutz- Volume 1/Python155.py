class tested:
    def __init__(self,num):
        self.state=num
    def sample(self,number):
        print(number,self.state)
        self.state+=1
s=tested(1)
s.sample("Wow");