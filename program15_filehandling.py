import os
if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
else:
    print("file does not exist")

#csv- comma seprated file-