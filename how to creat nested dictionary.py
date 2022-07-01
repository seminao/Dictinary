# a={}
# user=("enter the number")
# a[user]={}
# age=input("enter the age")
# c=input("enter the class")
# a[user][age]=age
# a[user][c]=c
# print(a)

# a={}
# name=input("enter the name")
# a[name]={}
# # hair=input("enter the hair ")
# c=input("enter the hair color")
# a[name]["hair color"]=c
# print(a)

# a={}
# n=int(input("enter the no"))
# a[n]={}
# name=input("enter the number")
# a[n][name]={}
# hair=input("enter the hair ")
# c=input("enter the hair color")
# a[n][name][hair]=c
# print(a)

# a={}
# u=int(input("enter the number"))
# i=0
# while i<3:
#     name=input("enter the name")
#     hair=input("enter the hair color")
#     eye=input("enter the eye color")
#     age=(input("enter the age"))
#     a[u]={}
#     a[u][name]={}
#     a[u][name]["hair color"]=hair
#     a[u][name]["eye color"]=eye
#     a[u][name]["age"]=age
#     u=u+1
#     i+=1
# print(a)
# (d={occurance:{a:2,b:3,c:2:d:1} hyna puthoktoua
a="abcd"
b={}
e={}
u=(input("enter the word"))
for i in a:
    if i in b:
        b[i]+=1
    else: 
        b[i]=1
e[u]=b
print(e)