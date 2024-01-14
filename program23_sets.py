set1= {10,20,30,"python"}
print(set1)
#print(set1[1]) # give error because there is no index number in set
#set1[2]="java" # error
set1.add("java")
print(set1)
set2={"apple","banana","kiwi","orange","apple"}
print(set2)
# no error, it will just ignore the duplicate value.