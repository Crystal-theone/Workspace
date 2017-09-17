fileObj=open("Files\\BinaryFile.bin","wb+");
s=bytearray(b"Akay this is a simple binary file.\n and this is the second line.\n");
fileObj.write(s);
fileObj.flush();
fileObj.seek(0);
s=fileObj.readline();
print((s[0:4]).decode())
print(s[0:4][0])
