class Animal:
    def __init__(self,name,age):
         self.name=name
         self.age=age

    def showdata(self):
         print("name and age is",self.name,self.age)

class Dog(Animal):
    def __init__(self,breed):
        self.breed=breed

    def datashow(self):
        print("we are child  dog class ND breed is ", self.breed)

obj1=Dog("bulldog")
obj1.datashow()
obj2=Animal("tommy",10)
obj2.showdata()