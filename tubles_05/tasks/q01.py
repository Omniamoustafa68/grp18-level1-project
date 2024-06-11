print('--remove duplicates from a list of tuples---')

ips_list = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
unique_list = []

for item in ips_list:
    if item not in unique_list:
       unique_list.append(item)
print(unique_list)



