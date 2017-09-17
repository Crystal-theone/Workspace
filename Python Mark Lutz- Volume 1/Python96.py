from collections import  namedtuple
Employee=namedtuple("Employee",["Id","Name","Rank"]);
e1=Employee(1,"Uzair Tariq","S");
print(e1[0]);
d=e1._asdict();
print(d)
print(d["Name"]);
x=1,2,3,4;
print(x);
a1,b2,c3=e1;
print(a1);
print(b2);
print(c3);