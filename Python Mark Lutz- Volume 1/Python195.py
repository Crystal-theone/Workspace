def permutation(sequence):
    if not sequence:
        print("Returned Result ",sequence)
        yield sequence
    else:
        for i in range(len(sequence)):
            rest=sequence[:i]+sequence[i+1:]
            print("Rest of Sequence ",rest)
            g=permutation(rest)
            print("Inner Permutation::",list(g))
            for x in g:
                print("Yielded Value ",x," Rest Value::",rest)
                yield sequence[i:i+1]+x
for x in permutation(['a','b']):
    print(x)
