di={1:"Uzair","2":"Ali",3:"Rizwan",55:"Ahmed"};
print(di)
for keys in di:
    print(str(keys)+"\t"+di[keys])
print(di.keys())
print(di.items())
print([name for (id,name) in di.items() if id==55])
di[("uzair","1993")]="Okay i was born on this date";
print(di)
print(di[(("uzair","1993"))])
if (1,"Uzair") in di.items():
    print("Value present");
d3=dict(name="Vov",val="s");
