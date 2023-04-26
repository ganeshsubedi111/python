# list in python
# list always declare in square bracket[] it is mutable(means change,delete)
# inside list element comes in comma ,separate
# we can create list , dictionary or tuple inside list

# integer list
'''
intlist=[1,2,3,[4,5,6]] # nested listed
print(type(intlist), intlist)
print(intlist[1])
print(intlist[3][1])
print(intlist[0:])
print(intlist[0: : 2])
'''

# List iteration
print("length of list:")
l=[1,5,9,13,14,15,19,21]
t=len(l)
print(t)

print("Accesing each element of list:")
# for a in range(t):
#     print(l[a])


for a in l:
 print(a)

 
print("After Reversing list element:")
 # reverse print list
for a in range(t-1,-1,-1):
 print(l[a])