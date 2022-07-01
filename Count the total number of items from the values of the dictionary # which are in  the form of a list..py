# 1st**Count the total number of items from the values of the dictionary
# which are in  the form of a list.
d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c = 0
for i in d.values():
   for v in i: 
       c += 1
print(c)

# **2nd
d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
total = 0
for v in d:
    v_l= d[v]
    c = len(v_l)
    total += c

print(total)
