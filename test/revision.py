'''import os
#folder== directory
print(os.getcwd())# get current working directory
os.chdir("test") # change directory
print(os.getcwd())
#os.makedirs("demo1") # to make directory
#os.rename("demo","newdemo")
os.removedirs("demo1")
'''
# files
import sys
with open("test/hello.txt","w") as file:
    content=file.read()
    print(content)
    file.write("we are writing in.....")
    content=file.read()
with open("test/hello.txt","r") as file:
    content=file.read()
    print(content)
    

