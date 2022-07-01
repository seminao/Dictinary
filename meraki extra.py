# *o/p=1
# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# *key error
# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])


# **count occurent
# fruit = {}
# def my(i):
#     if i in fruit:
#         fruit[i]+=1
#     else:
#         fruit[i]=1
# my('Apple')
# my('Banana')
# my('apple')
# my('Apple')
# print(len(fruit))
# print(fruit)

# *o/p=1
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print(len(Details["Student"])) 

# *error
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))


# *o/p=30
# o/p={(1,2,4):8,(4,2,1):10,(1,2):12}
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#  sum += my_dict[k]
# print(sum)
# print(my_dict)



