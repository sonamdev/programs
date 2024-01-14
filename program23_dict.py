dict1={
    "BT001":"english",
    "BT002":"Maths",
    "BT003":"C programming",
    324:"python"

}

dict1.update({"BT004":"c#"})
print(dict1)
dict1.update({112:"manasa"})
print(dict1)
dict1.pop(324)
dict1.clear()
print(dict1)
del dict1
#print(dict1)  # will give error beacuse dictionary is deleted