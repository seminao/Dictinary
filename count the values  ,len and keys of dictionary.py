# **values
meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
b=len(meal.values())
print(b)

# **keys
meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
b=len(meal.keys())
print(b)

# ** first method for len
# using len method
# o/p=3
meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
print(len(meal))

# **second method for len
d={1:'a',2:'b'}
c=0
for i in range(len(d)):
   c=c+1
print (c)
