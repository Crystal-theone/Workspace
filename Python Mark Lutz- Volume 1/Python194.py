def permutation(sequence):
    if not sequence:
        print("Sequence is empty")
        return [sequence]
    else:
        res=[]
        for i in range(len(sequence)):
            rest=sequence[:i]+sequence[i+1:]
            print("Outer Loop ",rest)
            for x in permutation(rest):
                print("Inner Executed",x)
                res.append(sequence[i:i+1]+x)
                print("Inner Loop ",res," X:",x," Over all sequence ",sequence)
        print("Returned Result ",res)
        return res
print("Final Result:: ",permutation(list(range(10))))