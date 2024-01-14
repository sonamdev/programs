class Animal:
    type='mammal'
    
    def __init__(self,name):
        self.name=name
        print("inside constuctor",self.name)
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("inside constuctor",self.name)
        print("inside constuctor",self.age)
    
obj1=Animal("dog",10)
obj2=Animal("cat",20)
obj3=Animal("camel",15)

print(obj1.type)

