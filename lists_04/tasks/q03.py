numbers_list = [1, 6, 3, 5, 3, 4]
num = 6
is_found = False     #flag
for i in range(len(numbers_list)):
    if num == numbers_list[i]:
        print(num,'is found on index =', i)
        is_found = True

if not is_found :        #is_found == False
   print(num, ' is not found in the list')





