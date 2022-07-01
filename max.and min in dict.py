# taking out max 
# a={"a":57,"b":10,"c":2,"d":40,"e":25}
# max=0
# for v in a:
#     if a[v]>max:
#         max=a[v]
# print(max)

# **min
# a={"a":57,"b":10,"c":2,"d":40,"e":25}
# s=min(a.keys())
# print(s)

# **taking out the max value of keys
# e= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# max=0
# sec=0
# th=0
# rd=0

# d=[]
# for  i in e:
#     for v in e:
#         if e[v]>max:
#             max=e[v]
#             a=v
#         if e[v]>sec and e[v]<max:
#             sec=e[v]
#             b=v
#         if e[v]>rd and e[v]<sec:
#             rd=e[v]
#             c=v
#         if e[v]>th and e[v]<rd:
#             th=e[v]
#             f=v
# d.append(a)
# d.append(b)
# d.append(c)
# d.append(f)
# print(d)


# *taking out the higest three values
# d={'a':210, 'b':58, 'c':101,'d':40, 'e':100, 'f':20}
# a=[]
# b=[]
# max1=0
# max2=0
# max3=0
# for i in d:
#     b.append(d[i])
#     i=0
#     while i<len(b):
#         if b[i]>max1:
#             max1=b[i] 
#         elif max1>b[i] and max2<b[i]:
#             max2=b[i]  
#         elif  max1 and max2>b[i] and max3<b[i]:
#             max3=b[i]
#         i=i+1
# a.append(max1)
# a.append(max2)
# a.append(max3)
# print(a)



# **taking out the 3 highest values using slycing
# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# a=[]
# for v in my_dict:
#     b=my_dict[v]
#     a.append(b)
# a.sort()
# print(a[3:])

# **taking out the 4 highest values
# e= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# max=0
# sec=0
# rd=0
# th=0
# for i in e:
#     for v in e:
#         if e[v]>max:
#             max=e[v]
#         elif e[v]>sec and e[v]<max :
#             sec=e[v]
#         elif e[v]>rd and e[v]<sec:
#             rd=e[v]
#         elif e[v]>th and e[v]<rd:
#             th=e[v]
# print("max=",max,"\n""sec=",sec,"\n""rd=",rd,"\n""th=",th)


# **taking out the 4highest values including keys:
e= {'a':50, 'b':58, 'c':56,'d':80, 'e':100, 'f':20}
max=0
sec=0
th=0
rd=0
for  i in e:
    for v in e:
        if e[v]>max:
            max=e[v]
        if e[v]>sec and e[v]<max:
            sec=e[v]
        if e[v]>rd and e[v]<sec:
            rd=e[v]
        if e[v]>th and e[v]<rd:
            th=e[v]
print(max,sec,rd,th)


