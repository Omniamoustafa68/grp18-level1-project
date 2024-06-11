# employee basic data
employee_id = 101
employee_name = 'omnia moustafa'
employee_salary = 7000.55
employee_job = 'python developer'

print('-----concat string to string----')
print(employee_name + ' work as ' +employee_job)

print('-----concat string to int-----')
print(' data tybe from int to string --- [casting] ----')
print(employee_name + ' his id =  ' + str(employee_id))

print('----concat string to float -----')
print('---- convert data type from float to string ------- [casting] -----')
print(employee_name + 'takes salary = ' + str(employee_salary))

print('----convert from float to int ------ [casting] ----')
print(employee_salary)
print(type(employee_salary))
print('---')
new_salary = int(employee_salary)
print(new_salary)
print(type(new_salary))