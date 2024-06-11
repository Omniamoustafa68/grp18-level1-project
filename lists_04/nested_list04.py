
print('----- program to show nested lists -------')

my_nested_list = [
                   [101, 'Ahmed', 7000.0],
                   [102, 'Marwa', 5000.0]
                 ]
print(len(my_nested_list))
print(my_nested_list)

print(my_nested_list[0])  # [101, 'Ahmed', 7000.0]

print(my_nested_list[1]) # [102, 'Marwa', 5000.0]

print(my_nested_list[1][1]) # Marwa

print(my_nested_list[0][2]) # 7000.0

my_nested_list.append([103, 'Ehab', 10000.0])
print(my_nested_list)

print(my_nested_list[2][1])  # Ehab

new_nested_list = [
                   [101, 'Ahmed', 7000.0, ['cairo', 'nasr city', '11851']],
                   [102, 'Marwa', 5000.0, ['giza', 'maadi', '24562']]
                 ]

print(new_nested_list[0][3][1])  # nasr city
print(new_nested_list[1][3][0])  # giza

# slicing
numbers_list = [16, 5, 20, 13, 2, 14, 30, 20, 70, 20]
print(numbers_list[:5])

print('---slicing---')
numbers_list = [16, 5, 20, 13, 2, 14, 30, 20, 70, 20]
print(numbers_list[0]) 			# the first index : 16
print(numbers_list[-1]) 			# the last index : 20
print(numbers_list[0:5]) 			# from index 0 to 4 : [16, 5, 20, 13, 2]
print(numbers_list[:5])  			# from index 0 to 4 : [16, 5, 20, 13, 2]
print(numbers_list[:-1])			# from the index 0 to the index before the  #last [16, 5, 20, 13, 2, 14, 30, 20, 70]
print(numbers_list[6:]) 			# from index 6 to end : [30, 20, 70, 20]]
print(numbers_list[-4:])  			# from index -4 to end : [30, 20, 70, 20]
print(numbers_list[0:8:2]) 			# from index 0 to 7 - step 2 : [16, 20, 2, 30]
print(numbers_list[:]) 	# copy		# from 0 to end - same copy : [16, 5, 20, 13, 2, 14, 30, 20, 70, 20]
print(numbers_list[::-1]) 			# from 0 to end - step - 1 = print string in 	# reverse order : [20, 70, 20, 30, 14, 2, 13,  20, 5, 16]

