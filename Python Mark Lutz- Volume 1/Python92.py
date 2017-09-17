dic1=dict(name="Uzair",last="Tariq");
print(list(dic1.keys()))
d=list(dic1.items());
print(d)
print(d[0][0]);
for k in dic1.keys():
    print(dic1[k]);
vals=dic1.values();
print(list(vals));
dic1["name"]="Senuch";
print(dic1)
print(list(vals))