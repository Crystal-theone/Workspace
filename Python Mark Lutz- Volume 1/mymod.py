def countLines(filename):
    d=open(filename,'r+');
    return len(d.readlines())
def countCharacters(filename):
    f=open(filename,'r+')
    return len(f.read())
def test(filename):
    print "Lines Count : "+str(countLines(filename))
    print "Character Count : "+str(countCharacters(filename))
if __name__=="__main__":
    sum(2)
    test("mymod.py")