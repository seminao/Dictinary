# Q20.Write a Python program to check a dictionary is empty or not.
d={1:1,2:2,3:3}
e={}
for i in d:
    if d[i] not in e:
        print("empty")
        break
    else:
        print("not empty")
        break