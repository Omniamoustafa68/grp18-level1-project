print('-- calculate sum of salary of all employees--')
company_employees = [
    (101, 'ahmed esam', 10000.0, 'cairo'),
    (102, 'ibrahim ahmed', 9000.0, 'cairo'),
    (103, 'adham aly', 5000.0, 'cairo'),
    (104, 'islam hassan', 7000.0, 'cairo')
]
total=0
for item in company_employees:
    total = total + item[2]
print('sum = ', total)
