#**first method
d={10:1,20:2,30:3,40:4}
o = {}
for k,v in d.items():
    if k in o:
        o[k].append(v)
    else:
        o[k] = [v]
print(o)

# **second method
d={10:1,20:2,30:3,40:4}
o = {}
for k,v in d.items():
    o[k]=[v]
print(o)

