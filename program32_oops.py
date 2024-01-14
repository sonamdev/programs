class Person:
    def showVlaues(self):
        print("we are in person class")

class Student(Person):
    def showCase(self):
        print("we are in Student class")
class Employee(Person):
    def showData(self):
        print("we are in Employee class")

class Junior_employee(Employee):
    def dataValue(self):
        print("we are in junior employee class")

job1=Junior_employee()
job1.showData()
"""job2=Junior_employee()
job2.showCase() # give error
"""
eobj1=Employee()
eobj1.showData()
eobj1.dataValue()# give an error because u cant go from parent to child




