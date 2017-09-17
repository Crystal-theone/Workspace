list=["Uziar7","Ali5","Umar7","Rizwan2","Usman1"];
compre=[data for data in list if data[0]=='U'];
print(compre);
compre2=[data for data in list if data[-1].isdigit()]
print(compre2)
compre2=compre2[:3];
mix=[a+b for a in compre for b in compre2];
print(mix);
