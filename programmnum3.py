import numpy as np
a=np.array([10,20,30,40,50,60])
print(type(a))
print(a[1:5])
print(a.shape)
for i in a:
    print(i+5)
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

for x in arr:
    for y in x:
        print(y+5)

arr1=np.array([8,-4,5,7,2,1])
print(np.sort(arr1))
print(np.abs(arr1))
print(np.max(arr1))