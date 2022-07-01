# **taking out values and keys in list
dic={1:2,2:4,5:6}
d={}
for j in dic.values():
    d[j]=list(dic.keys())
print(d)
