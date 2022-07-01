# *first method
# *if we enter keys getting output both keys and values
p={1:2,2:3,3:4,4:5}
s=int(input("enter the keys"))
e={}
for i in p:
    c=p.get(s)
    e[s]=c
print(e)

# *second method
# p={1:2,2:3,3:4,4:5}
# s=int(input("enter the keys"))
# e={}
# for i in p:
#     if s in p.keys():
#         e[s]=p[s]
# print(e)

