# # chr() and ord()- function of string
# #chr()-return character 
# print(chr(65))
# y=chr(120)
# print(type(y),y )

# #ord()-return asci value
# y=ord('A')
# print(type(y),y)


# format function in python-string format() method
a= "welcome {} {} to the {}  class".format("Ganesh","subedi","python")
print(a)
a= "welcome {0} {1} to the {2}  class".format("Ganesh","subedi","python")
print(a)
a= "welcome {firstname:>10} {lastname:<10} to the {course}  class".format(firstname="Ganesh",lastname="subedi",course="python")
print(a)