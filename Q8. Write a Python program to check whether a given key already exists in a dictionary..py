# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.

d={9:2,8:3,7:4,6:5}
user=int(input("enter the keys"))
for i in d:
    if user in d.keys():
        print("keys  already exits")
        break
    else:
        print("not yet exits")
        break


