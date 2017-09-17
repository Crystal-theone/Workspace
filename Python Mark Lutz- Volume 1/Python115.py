import sys
file=open("Files\\Cross.txt",'w');
sys.stdout=file;
print("Wow");
file.close();
sys.stdout=sys.__stdout__;
print(open("Files\\Cross.txt").read())