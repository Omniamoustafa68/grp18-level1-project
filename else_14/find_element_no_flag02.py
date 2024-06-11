#program to find element in a list if found : print it is found
#if not found print elemeny is not found
#using no flag

my_list = [15, 14, 10, 16,20]
num = 11
for item in my_list:
    if item == num:
        print('num is found in index', my_list.index(num))
        break
else: # execute if loop complete without break
    print('num is not found')