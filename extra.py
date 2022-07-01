# Dictionary Built-in Functions
# squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: False
# print(all(squares))

# Output: True
# print(any(squares))

# Output: 6
# print(len(squares))

# Output: [0, 1, 3, 5, 7, 9]
# print(sorted(squares))

# using len method
# o/p=3
# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# print(len(meal))

#taking out only one values:
# a={"name":"onring","age":99}
# print(a["name"])

# *to find both keys and value
# a={"name":"onring","age":99}
# for i,j in a.items():
#     print(i,j)

# **to find only values
# *o/p=oring
    # 99
# a={"name":"onring","age":99}
# for i in a.values():
#     print(i)

# **find only keys
# a={"name":"onring","age":99}
# for i in a.keys():
#     print(i)

# *without methods taking out values
# a={"name":"onring","age":99}
# for i in a:
#     print(a[i])

# *without methods taking out keys
# a={"name":"onring","age":99}
# for i in a:
#     print(i)

# **taking out only keys
# e= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# print(e.keys())

# *counting the len of dic
# dict= {1: 'A', 2: 'B', 3: 'C'}
# c=0
# for i in dict:
#     c=c+1
# print(c)
