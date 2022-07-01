# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# dic={}
# for i in range(len(list1)):
#     dic[list1[i]]=list2[i]
# print(dic)

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
dic={}
for i in range(len(list1)):
    dic.update({list2[i]:list1[i]})
print(dic)

# l=["one","two","three"]
# user=int(input("enter the user"))
# i=0
# e={}
# while i<len(l):
#     e[l[i]]=user
#     i=i+1
# print(e)
