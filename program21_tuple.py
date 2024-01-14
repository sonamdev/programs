meeting =("archana","manasa","shashank","sonam","python")
# update value in a tuple

print(meeting)
print("meeting tuple before update")
print(id(meeting))
#step1- convert tuple into list-
meeting_list=list(meeting)
print(type(meeting_list))
print(meeting_list)
#step2- update ur list
meeting_list.append("ruthvik")
print(meeting_list)
#step3 convert list back to tuple

meeting= tuple(meeting_list)
print(meeting)
print("meeting tuple after update")
print(id(meeting))
