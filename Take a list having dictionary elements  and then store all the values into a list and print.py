# **Take a list having dictionary elements  and then store all the values into a list and print.
# d=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# i=0
# a={}
# while i<len(d):
#     a.update(d[i])
#     i+=1
# b=[]
# for j in a.values():
#     b.append(j)
# print(b)


# **Take a list having dictionary elements  and then store all the unique values into a list and print.
d=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=0
a={}
while i<len(d):
    a.update(d[i])
    i+=1
print(a)
