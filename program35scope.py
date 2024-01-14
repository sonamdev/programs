#Scope
x=100 # Global variable

def showdata():
    #global x
    global y
    y=10 
    print(y)
    x=10
    print(x)

print(x)

showdata()