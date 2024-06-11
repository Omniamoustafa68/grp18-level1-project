#program to show how to handle exception
try:
    first_number = int(input('please enter first number: ') )
    second_number = int(input('please enter second number : ') )
    open('c:\\my_files\\egypt.txt')
    result = first_number / second_number
    print('result = ', result)
except ValueError as e:
    print('please enter only number',e)
except ZeroDivisionError as e:
    print('cannot divide zero ', e)
except Exception as e:
    print('there is something wrong - please contact administrator', e)
finally:
    print('this is the finally section - must be executed')
print('--- continue or end program')