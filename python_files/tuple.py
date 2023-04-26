# tuple-tuple are immutable(value inside tuple cannot be change)
t=(1,2,3,4,2,5,2,1,6,4,8) 
print("length of tuple is:")
l=len(t)

print(l)
for a in range(l):
    print(t[a])

print("The  2 repeat in the tuple following times:")
b=t.count(2)
print(b)

print("the index of 4 is:")
c=t.index(4)
print(c)
