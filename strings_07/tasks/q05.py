print('--develop a program that checks whether a given string a plindrome or not--')
str1= '1 2 5 2 1'
print(str1)
numbers_list = str1.split()
numbers_list.reverse()
after_reverse = ' '.join(numbers_list)
print(after_reverse)

if str1 == after_reverse:
    print('it is plindrome')
else:
    print('it is not plindrome')

