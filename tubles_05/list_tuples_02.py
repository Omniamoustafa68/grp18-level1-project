print('--program to show list of tuples---')
ips_list =[
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('129.168.0.24', 'n'),
    ('129.168.0.81', 'n'),
    ('129.168.0.11', 'y'),
]

print(ips_list)
print(type(ips_list))

#('192.168.0.22', 'y')
print(ips_list[1])

#'192.168.0.22'
print(ips_list[1][0])

print('---loop for each --- print only ip has (y)')

for item in ips_list:
    if item[1]=='y':
        print(item, item[0][-2:])

print('---- loop index -- print only ip has (y) ')

for i in range(len(ips_list)):
    if ips_list[i][1]=='y':
        print(ips_list[i], ips_list[i][0][-2:])
