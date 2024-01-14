list1=[1,3,4,8,9,10,44,88,12,5,77]
# reverse the list
print(list1[::-1]) # method 1
list2=[]
#method3-
for i in list1:
   print(i)
   list2= [i] + list2 # concatinnating 2 lists
print(list2,"list2....")



"""
list1=[1,3,4,8,9,10,44,88,12,5,77]
list1.reverse() #method2 by manasa
print(list1)
"""

