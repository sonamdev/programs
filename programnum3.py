import numpy as np
arr=np.array(["archana","manasa","sonam"])
print(arr.dtype)
arr1=np.array([1.2,2.3,5.6])
print(arr1.dtype)
arr2=np.array([1,2,3,4,5],dtype='S')
print(arr2)

arr3=arr1.astype('i')# converting datatypes
print(arr3)

x=arr1.copy()
print(x)
print(x.shape)
x1=x.reshape(3,1)
print(x1)
for i in arr1:
    print(i+5)

ar=np.array([[1,2,3],[3,4,5]])
for i in ar:
    #print(i)
    for j in i:
        print(j)