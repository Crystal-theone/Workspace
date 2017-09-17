import pickle;
data={1,2,3,4,5,5,6};
print("Printing Data to be written");
print(data);
with open("Files\\Storage6.txt","wb") as myFile:
    pickle.dump(data,myFile);
with open("Files\\Storage6.txt","rb") as myFile:
    data2=pickle.load(myFile);
print(data2);