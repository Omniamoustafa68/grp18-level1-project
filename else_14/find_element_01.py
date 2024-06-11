#program to find element in a list if found : print it is found in index
#if not found print element is not found
#using flag
my_list = [15, 14, 10, 16, 20]
num = 11
is_found = False
for i in range(len(my_list)):
    if my_list[i] == num:
        is_found= True
        print('num s found at index = ', i)
        break
if is_found == False:
    print('num is not found')