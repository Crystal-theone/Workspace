dictionary={'a':1,'b':2,'c':3,'d':4}
print("Before Processing Dictionary");
print(dictionary);
if not 'f' in dictionary:
    print("Soory no data relate to the query found!\nInsert data[Y//N]");
    localInput=input();
    if localInput=="Y":
        dictionary['f']=input("\nEnter value::");
    else:
        print("Program Quitted");
print(dictionary)