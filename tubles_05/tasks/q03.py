company_employees=[
    (101, 'hayam esam', 10000.0, 'engineer', 'F'),
    (102, 'ibrahim ahmed', 9000.0,'accountant','m'),
    (103, 'adham aly', 5000.0, 'engineer', 'm'),
    (104, 'islam hassan', 7000.0, 'sales', 'm'),
    (105, 'marwa esam', 7000.0, 'marketer', 'F'),
    (106, 'ola hassan', 7000.0, 'engineer', 'F')

]
male_count = 0
female_count = 0
for i in range(len(company_employees)):
    if company_employees[i][4] == 'F':
        female_count= female_count+1
    elif company_employees[i][4] == 'm':
        male_count= male_count+1
print('female count = ', female_count)
print('male count = ', male_count)


