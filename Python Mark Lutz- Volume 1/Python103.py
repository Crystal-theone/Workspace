lis=["Uzair","Tariq"];
dict={"name":lis,"age":23,"father":"Tariq Mahmood"};
print(dict);
import json;
json.dump(dict,open("Files\\Storage4.json","w"),indent=5);
print("File Written");
dataHolderObject=json.load(open("Files\\Storage4.json"));
print(dataHolderObject);