# polymorphisim  in python -overloading and overriding
a=[1,2,3]
print(len(a))

b="welcome"
print(len(b))

print("-----------overloading----------\n")
print("this is a------ example of overloading---------\n")
class hello:
    def displayhello(self,name=""):
        print("welcome to the python course"+name)

obj=hello()
obj.displayhello()
obj.displayhello("hello user")

print("-----------overiding----------\n")
print("this is a-------- example of overriding------\n")
class hello:
    def displayhello(self):
        print("welcome to the python course")

class hello1(hello):
    def displayhello(self):
        super().displayhello() # calling hello class function
        print("hello user")
obj=hello1()
obj.displayhello()
        