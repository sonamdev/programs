print(2+2) #  operator is adding the value
print("hello"+"world") # + operator is concatinating the values
print(6-2)
#print("hello"-"world")
print("hello")
print("world",sep='%')
def experiment():
    print("no value")
def experiment(name):
    print("taking name",name)

experiment("sonam")

class Demo:
    def __init__(self):
        print("we are in default init")
#overriding
    def __init__(self,name):
        self.name=name
        print("we are taking name argument",self.name)

o1=Demo("sonam")# constructor overloading, which is absent
#o2=Demo() # generate error