d=dict(a="a",b="b",c="c");
d2=dict(a="a",b="z",c="c");
if sorted(d.items())<sorted(d2.items()):
    print("d2 is greater");
elif sorted(d.items())>sorted(d2.items()):
    print("d is greater");
s="str"*3;
print(s)