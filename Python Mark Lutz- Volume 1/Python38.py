import struct
data=struct.pack('i5s5s',7,b'Uzair',b'Tariq')
print(data)
file=open('Files\\BinaryFile.bin','wb');
file.write(data);
file.close();
file=open('Files\\BinaryFile.bin','rb');
data=file.read();
print(data);
print(list(data))
print(struct.unpack('i5s5s',data))