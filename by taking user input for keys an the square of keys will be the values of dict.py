user=int(input("enter the number"))
i=0
c=[]
while i<=user:
    d=int(input("enter the number"))
    c.append(d)
    a=c
    i=i+1
e={}
j=0
while j<len(a):
    e[a[j]]=a[j]*a[j]
    j=j+1
    f=e
    s=0
    for v in f:
        s=s+f[v]
print(e)

# **another method
d=[1,2,3,4,5,6,7]
b={}
i=1
while i<=len(d):
    c=i*i
    b[i]=c
    i+=1
print(b)
