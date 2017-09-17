def sequencesCheck(obj1,obj2):
        ls=[];
        for x in obj1:
            if x in obj2:
                ls.append(x)
        return ls
s="uzair"
s2="riaz"
res=sequencesCheck(s,s2)
print(res)