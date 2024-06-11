print('-- program to show list of dictionary---')
student_list=[{101:'ahmed', 102:'marwa', 103:'mostafa'}]
print(len(student_list))   #1

print(student_list[0]) #{101:'ahmed' , 102:'marwa', 103:'mostafa}

print(student_list[0][102])   #marwa

#marwa> marwa mostafa
student_list[0][102] ='marwa mostafa'
print(student_list)
print('----------------')
students_dict2 = {104:'ayman' , 105:'ibrahim'}
student_list.append(students_dict2)
print(student_list)
print(student_list[1][105])   #ibrahim