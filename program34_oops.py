class Student:
    def Sname(self,name):
        print("the name of the student is -",name)
# having same signature
class pyStudent(Student):
    x=10
    name="manasa"
    #over riding in inheritence
    def Sname(self,name):
        print("the name of the python student is -",name)

    def marks(self,n):
        print(n)

pobj1=pyStudent()
pobj1.marks(10)
pobj1.Sname("shshank")