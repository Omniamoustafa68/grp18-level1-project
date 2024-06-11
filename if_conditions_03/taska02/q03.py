import random

print('--- conditional equation --- ')
#input

print('1 = +')
print('2 = -')
print('3 = * ')
print('4 = /')
#operator input
user_input_operator = input('enter the operator numbers:')
user_input_operator = int(user_input_operator)
# first_number input
first_number = input('enter the first number :')
first_number=int(first_number)
# second_number input
second_number= input('enter the second number :')
second_number=int(second_number)

if user_input_operator == 1 :
    result= first_number + second_number
    print('result = ', result)
elif user_input_operator == 2 :
    result = first_number - second_number
    print('result = ',result)
elif user_input_operator == 3 :
    result = first_number * second_number
    print('result = ', result)
elif user_input_operator == 4 :
    result= first_number / second_number
    print('result = ', result)



