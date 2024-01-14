n=100
class A:
    #__name="Archana"
    #print(__name)
    def __init__(self,age):
        self.__age=age
        
        print("the age is ",self.__age)


    def showdata():
        print("clearing doubts")

#lets create object of this class
a1=A(10)
a1.showdata
def archanadata():
    print("hi archana")
    ar=50 #local

#private default public

class AA:
    def __init__(self) :
        print("inside mamals")

    def specality(self):
        print("mamals take o2 from air")
class BB(AA):
    def walk(self):
        print("homosapiens acan walk")

class CC(AA):
    pass

class X(BB,CC):
    pass
