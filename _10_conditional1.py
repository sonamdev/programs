'''# condtional statement
num1=input("enter a number- ") # input is a string
num2= int(num1)
if num2 > 10:
    print("your number is bigger than 10")
else:
    print(" your number is not bigger")

######### take users age and name as input and verify whether the 
# user is able to vote or not?
name = input("please enter your good name- ")
age=int(input("enter your age- "))# type casting- from string to integer
if age > 18:
    print("you are eligible to vote")
else:
    print(" you are not eligible to vote")



'''

# student Grade system
StudentName=input("please enter your name - ")
percent=int(input("to enter your percentage- "))
if percent >80:
    print("A grade")
if percent >60:
    print("B grade")
if percent >45:
    print("C grade")
else:
    print("u failed the exam")
