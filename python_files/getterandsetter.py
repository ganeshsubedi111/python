#(getter and setter)
class person:
    def __init__(self):
        self.__name=""
    def getname(self):
        return  self.__name
    def setname(self,name):
        self.__name=name
obj= person()
obj.setname("hello")
name=obj.getname()
print(name)