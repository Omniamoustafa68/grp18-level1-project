print('--main tuple operations---')

print('--creat and print tuple--')
my_tuple= (101, 'ahmed mahfouz', 8000.0, 'nasr city - cairo')
print(my_tuple)
print(type(my_tuple))

print('---access element in a tuple by index []---')
#nasr city - cairo
print(my_tuple[3])
#my_tuple[3] ='madi'     error
#print(my_tuple)

print('--un packing tuple---')
person_id, person_name, person_salary, person_address = my_tuple
print(person_name, person_address)


print('--loop over tuple---')
for i in range(len(my_tuple)):
    print(my_tuple[i])

print('--------')

for item in my_tuple:
    print(item)
