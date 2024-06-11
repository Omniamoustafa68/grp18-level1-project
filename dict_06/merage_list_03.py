print('--program to merage ')
emp_ids_list=[101, 102, 103]
emp_names_list=['ahmed', 'salma ', 'omar']

person_dict = {}
for i in range(len(emp_ids_list)):
     person_dict[emp_ids_list[i]] = emp_names_list[i]
print(person_dict)