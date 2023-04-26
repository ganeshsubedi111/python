# delete function:
# del ,pop(), remove() ,clear()

# l=[1,3,5,7,9,11,13,15,17]
# print("it delete element from list:")
# del(l[2:5])
#print(l)

# print("it pop element respect to corresponding index from list:")
# l.pop(2)
# print(l.pop(2))
# print(l)

# print("it remove element from list:")
# l.remove(13)
# print(l)

# print("it clear all list:")
# l.clear()
# print(l)

# list function  for update element from list
# insert(), append(),extends()
'''
l=[1,3,5,7,9,11,13,15,17]
print("The original list is:",l)

print("list after inserting element:")
l.insert(0,0)
print(l)
l.insert(7,14)
print(l)

print("list after appending element:")
l.append(25)
print(l)
l.append(30)
print(l)
n=["apple","banana","Mango"]
l.append(n)
print(l)

print("list after extending element:")
n=["apple","banana","Mango"]
l.extend(n)
print(l)
m=["car","bike","cycle"]
l.extend(m)
print(l)
'''

# count()
print("the value is repeated following times:")
l=[10,20,25,30,35,10,45,65,20,50,35,45]
a=l.count(10)

print(a)

#max()
print("max value in list:")
b=max(l)
print(b)
#min()
print("min value in list:")
c=min(l)
print(c)
#sort()
print("list after sorting:")
l.sort()
print(l)
#reverse
print("list after reverse:")
l.reverse()
print(l)
#index
print(l.index(20))