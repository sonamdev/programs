#packing and unpacking of tuples
meeting =("archana","manasa","shashank","sonam") # packing
student1,student2,*student3=meeting #unpacking
print(student2)
print(student3)
print(type(student3))
