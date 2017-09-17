fileObj=open("Files\\Check.txt",'r+');
fileObj.write("Okay! This is my first interaction  with file.\n");
fileObj.write("and off course is the first example.!\n");
print(fileObj.tell());
fileObj.seek(0);
print(fileObj.tell());
print(fileObj.readline())