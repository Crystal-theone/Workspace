list=[123,'Uzair',"Sample"]
print(len(list))
list.append("Tariq");
print(list[len(list)-1])
print(len(list))
print("After Popping Variable")
list.pop(len(list)-1)
print(list.__len__())