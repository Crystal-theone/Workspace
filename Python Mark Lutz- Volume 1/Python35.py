tuple=(1,2,3,[4,5,6])
print(tuple)
tuple=(1,)+tuple[2:]
print(tuple)
for t in tuple:
    print(t)