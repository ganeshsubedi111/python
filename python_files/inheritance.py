# inheritance in python
# single inheritance
class A:
    def display(self):
        print("helo user from class A")

class B(A):
    def show(self):
        print("hello user from classB")

obj= B()
obj.display()
obj.show()

# multilevel inheritance


print(" multilevel inheritance:")
class A:
    def displayA(self):
        print("helo user from class A")

class B(A):
    def showB(self):
        print("hello user from classB")
    
class C(B):
    def showC(self):
        print("Hello user from calss C")

obj= C()
obj.displayA()
obj.showB()
obj.showC()

# multiple inheritance


print(" multiple inheritance:")

class A:
    def display_A(self):
        print("helo user from class A")

class B():
    def show_B(self):
        print("hello user from classB")
    
class C(A,B):
    def show_C(self):
        print("Hello user from calss C")

obj= C()
obj.display_A()
obj.show_B()
obj.show_C()