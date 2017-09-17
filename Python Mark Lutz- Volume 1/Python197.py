def myMapping(*sequence,padding=None):
    data=[list(x) for x in sequence]
    res=[]
    while any(data):
        res.append(tuple([(s.pop(0) if s else padding) for s in data]))
    return res
print(myMapping("abcddd","defg",padding="Bitches"))
