#Q1. Sample output: Counter({'a': 400, 'b': 400})
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# e={}
# for i in d1:
#     for j in d2:
#         if i==j:
#            d=d1[i]+d2[j]
#            e[i]=d
# print(e)



# Q3.Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
# user=int(input("enter the number"))
# i=0
# e={}
# while i<(user):
#     user2=int(input("enter the number"))
#     d=user2*user2
#     e[user2]=d
#     i=i+1
# print(e)

#Q5. Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

# *descending order by value 
# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# p=sorted(d.values())
# a=p[::-1]
# e={}
# for i in a:
#     for j in d.keys():
#         if d[j]==i:
#             e[j]=i
# print(e)

# *ascending order by value
# o/p:[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# p=sorted(d.values())
# a=[]
# for i in p:
#     for j in d.keys():
#         if d[j]==i:
#             c=j,i
#             a.append(c)
# print(a)

# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# b=[]
# for i in d.items():
#     b.append(i)
# print(b)

# Q6.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# d={0:10,1:20}
# e={}
# e1={}
# s=0
# for i in d:
#     if i not in e:
#         e[i]=d[i]
#     s=s+d[i]
#     e1[i+1]=s
# j={**e,**e1}
# print(j)


# 0/p:[5,6,3,2,1,0,4]
# l=[4,2,7,8,10,20,6]
# i=0
# a=[]
# while i<len(l):
#     j=0
#     c=0
#     while j<len(l):
#         if l[i]<l[j]:
#             c=c+1
#         j=j+1
#     i=i+1
#     a.append(c)
# print(a)

# Q7.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# *by using astric
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# d={**dic1,**dic2,**dic3}
# print(d)

# **by using update method
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# a=[]
# while i<len(l):
#     j=0
#     s=0
#     while j<2:
#         s=s+l[i][j]
#         d=s-l[i][-j]
#         j=j+1
#     i=i+1
#     a.append(d)
# print(a)


# Q13.Write a Python program to sum all the items in a dictionary.
# 1st method
# d={1:1,2:2,3:3,4:4,5:5}
# s=0
# s1=0
# e={}
# for i in d:
#     s=s+i
#     s1=s1+d[i]
#     e[s]=s1
# print(e)

# 2nd method
# d={1:1,2:2,3:3,4:4,5:5}
# s=0
# s1=0
# e={}
# for i in d:
#     s=s+i
#     s1=s1+d[i]
# e[s]=s1
# print(e)

# Q21.Write a Python program to print all unique values in a dictionary. 

# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#           {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#   {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in d:
#   for j in i.values():
#     if j not in b:
#       b.append(j)
# print(set(b))

# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:ac ad bc bd
# **1st method
# d={'1':['a','b'], '2':['c','d']}
# for i in d['1']:
#     for j in d['2']:
#         result=i+j
#         print(result)

# **2nd method
# d={'1':['a','b'], '2':['c','d']}
# i,j=d.values()
# for x in i:
#     for y in j:
#         print(x+y)

# Q26.
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

# d= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# i,j,k=d.keys()
# print(i,j,k)
# k,l,m=d.values()
# a=k
# b=l
# c=m
# f=a,b,c
# i=0
# while i<len(f):
#     print(a[i],b[i],c[i])
#     i=i+1

# Q27.Write a Python program to count the values associated with key in a dictionary.
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# Sample input if key is id: then 6

# d= [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# print(sum(i['id'] for i in d))
# print(sum(i['success'] for i in d))


# num_list = [1, 2, 3, 4]

# def fun(lista):
#     if len(lista) > 1:
#         return {str(lista[0]): fun(lista[1:])}
#     if len(lista) == 1:
#         return {str(lista[0]): {}}

# print(fun(num_list))

# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
# num_list = [1, 2, 3, 4]
# new_dict = current = {}
# for name in num_list:
#     current[name] = {}
#     current = current[name]
# print(new_dict)

# Q29.Write a Python program to sort a list alphabetically in a dictionary.
# l=["a","c","e","g","i","j","l","n","b","d","f","h","k","m"]
# l.sort()
# e={}
# i=0
# while i<len(l):
#     e[l[i]]=l[i]
#     i=i+1
# print(e)

# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dict:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dict:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 

# d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# e={}
# for k,v in d.items():
#     c=k.split()
#     e["".join(c)]=v
# print(e)

# 2nd method
# d = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
# d1= {}
# for i,j in d.items():
#     for x in " ":
#         i = i.replace(x,"")
#     d1[i]= j
# print(d1)

# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
# d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# max=0
# sec=0
# rd=0
# for k in d:
#     for v in d:
#         if d[v]>max:
#             max=d[v]
#             a=k
#         if d[v]>sec and d[v]<max:
#             sec=d[v]
#             b=k
#         if d[v]>rd and d[v]<sec:
#             rd=d[v]
#             c=k
# print(a,max)
# print(b,sec)
# print(c,rd)

# Q32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:
# key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# c=0
# print("key", "value", "count")
# for i in d:
#     c=c+1
#     print(i,"  ",d[i],"   ",c)

# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 
# d= {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i in d:
#     print(i)
#     for k,v in d[i].items():
#        c=k
#        print(c,":",v)

# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5
# d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# i,j=d.values()
# f=i+j
# c=0
# i=0
# while i<len(f):
#     c=c+1
#     i=i+1
# print(c)

# Q36.Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# d1={'key1': 1, 'key2': 3, 'key3': 2}
# d2={'key1': 1, 'key2': 2}
# for i in d1:
#     for j in d2:
#         if i==j and d1[i]==d2[j]:
#             print(i,":",d2[j],'is present in both d1,d2')
#             print('{}: {} is present in both d1,d2'.format(i,d1[i]))

# 0/p{10:[1],60[2,4],30[3],3[5]}
# dic={1:10,2:60,3:30,5:50,4:60,5:3}
# e={}
# for i in dic:
#     e[dic[i]]=i
# print(e)
# l=["123"]
# i=0
# while i<len(l):
#     a=[]
#     j=0
#     while j<len(l[i]):
#         a.append(int(l[i][j]))
#         k=0
#         while k<len(a):
#             s=a[k]**2
#             k=k+1
#         print(s)
#         j=j+1
#     i=i+1


# user=int(input("enter the number :"))
# i=1
# d={}
# while i<=user:
#     j=1
#     a=[]
#     while j<=10:
#         a.append(i*j)
#         d[i]=a
#         j+=1
    # i+=1
# print(d,end="")
# user=int(input("enter the number :"))
# i=1
# d={}
# while i<=user:
#     j=1
#     a=[]
#     while j<=10:
#         a.append(i*j)
#         d[i]={a}
#         j+=1
#     i+=1
# print(d,end="")

# l=[1,2,3,4,5,6,7,8,9,10]
# # o/p [2,4,6,8,10,1,3,5,7,9]
# # extend use twba yani
# i=0
# a=[]
# b=[]
# while i<len(l):
#     if l[i]%2==0:
#         a.append(l[i])
#     else:
#         b.append(l[i])
#     i=i+1
# f=a.extend(b)
# print(f)

# d={1:30,2:40,3:30,4:50}
# e={}
# e1={}
# a=[]
# for i in d:
#     if i==d[i]:
#         e[d[i]]=[i]
#     else:
#         e1[d[i]]=i
# k={**e,**e1}
# print(k)

# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
# d={'c1': 'Red', 'c2': 'Green', 'c3': None}
# e={}
# for i in d:
#     if d[i]!=None:
#         e[i]=d[i]
# print(e)

# Q39.Write a Python program to filter a dictionary based on values. 
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

# d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# e={}
# for i in d:
#     if d[i]>170:
#         e[i]=d[i]
# print(e)

# d={1:10,2:20,3:30,4:40}
# e={}
# for i in d:
#     e[d[i]]=[i]
# print(e)


# Q45.
# Write a Python program to remove a specified dictionary from a given list. 
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
# {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, 
# {'id': '#808000', 'color': 'Olive'}]
# d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
#     {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# remove='#FF0000'
# result=[]
# for i in d:
#     if remove in i.values():
#         pass
#     else:
#         result.append(i)
# print(result)

# Q47.
# A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary. 
# Original Dictionary:
# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# o/p:{'C1': [], 'C2': [], 'C3': []}
# a=[]
# e={}
# for i in d:
#     e[i]=[]
# print(e)
# d={'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'},
# # return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}
# e={}
# a=[]
# b={}
# for i in d:
#     if i==d[i]:
#         a.append(d[i])
#         b[d[i]]=a
#     else:
#         e[d[i]]=i
# d={**b,**e}
# print(d)
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# print(student_marks)
# query_name = input()
# x=student_marks[query_name]
# print(x)

# dic={1:10,2:60,3:30,5:50,4:60,5:30}
# a={}
# for key,value in dic.items():
#     if value not in a:
#         a[value]=[key]
#     else:
#         a[value].append(key)
# print(a)
d={1:10,2:60,3:30,5:50,4:60,5:30}
a={}
for i in d:
    if d[i] not in a:
        a[d[i]]=[i]
    else:
        a[d[i]].append(i)
print(a)