d={1:"mango",2:"apple",3:"ball"}
p=sorted(d.values())
a={}
for i in p:
    for j in d:
        if d[j]==i:
            a[j]=i
print(a)