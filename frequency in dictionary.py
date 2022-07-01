# ** by using print
a='the quick brown fox jumps over the lazy dog.'
a=a.split()
count={}
for i in a:
   if i in count:
      count[i]+=1
   else:
      count[i]=1
print(count)

# ** by using return
def my(a):
    a=a.split()
    count={}
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
print(my('the quick brown fox jumps over the lazy dog.'))

