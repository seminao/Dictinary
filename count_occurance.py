word="mississipi"
c={"m":0,"i":0,"s":0,"p":0}
for i in word:
    if i=="m":
        c["m"]+=1
    elif i=="i":
        c["i"]+=1
    elif i=="s":
        c["s"]+=1
    elif i=="p":
        c["p"]+=1
print(c)
    
# *2nd method
a="MISSISSIPPI"
d={}  
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

#Q2. Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
a='w3resource'
e={}
for i in a:
    if i in e:
        e[i]+=1
    else:
        e[i]=1
print(e)