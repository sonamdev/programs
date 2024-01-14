import random as r #aliasing
print(r.choice([1,2,3,4,5,6]))
print(r.randint(1,50))
print(r.random())
l1=[10,20,30,40]
r.shuffle(l1)
print(l1)