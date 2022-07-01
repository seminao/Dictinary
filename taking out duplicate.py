dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dict={}
for i,j in dic.items():
    if i and j not in dict:
        dict.update({i:j})
print(dict)

