dict_1 = {1: 'A', 2: 'B', 3: 'C'}
dict_2 = {}
for key in reversed(dict_1):
    dict_2[key] = dict_1[key]
print("dict_2: ", dict_2)