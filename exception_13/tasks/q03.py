try:
    first_numbers = int(input('please enter first number: '))
    second_numbers = int(input('please enter second number: '))
    result = first_numbers + second_numbers
    print(result)
except ValueError:
    print('please enter only number')