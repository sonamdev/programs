import re
#Regex- regular expression generation- 
sen="Hello everyone,how are u. The weather here is great here"
x=re.search("^Hello",sen)
x=re.search("here$",sen)
x=re.findall("here",sen)
x=re.split("\s",sen)
print(x)
