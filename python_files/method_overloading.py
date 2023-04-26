# method overloading and overriding in python
print("-----------method overloading----------\n")
class Area:
    def findarea(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None :
            print(x*x)
        else:
            print("nothing found")

obj=Area()
obj.findarea(10)
obj.findarea(10,20)
obj.findarea()


print("-----------method overriding----------\n")
class A:
    def showdata(self):
        print("i am in class A")

class B():
    def showdata(self):
        print("i am in class B")

obj=B()
obj.showdata() # override the class A