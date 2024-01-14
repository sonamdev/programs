a=int(input("enter a value- "))
b=int(input("enter b value - "))

try:
    print(" try...")
    c=a/b #critical statements
    print(" a/b is - ",c)
    #print(x)

except NameError:
    print("except1...")
    print(" no such variable x")

except:
    print("program failure..")
finally:
    print("a+b is ",a+b)