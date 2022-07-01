dict={"ap":[1,2,3],"pc":[4,5,6],"e":[6,7,1]}
for x in dict:
    i=0
    s=0
    while i<len(dict[x]):
        s=s+dict[x][i]
        i=i+1
    dict[x]=[s]
print(dict)