def add_numbers(x, y):
    return x + y


def subtract_numbers(x, y):
    return x - y


def multiply_numbers(x, y):
    return x * y


def divide_numbers(x, y):
    if y == 0:
        print('invalid')
    else:
        return x / y


# main_program
print('-- test addition function ----')
#addition = add_numbers(3, 5)
addition = add_numbers(x=3, y=5)
print(addition)

print('-- test subtract function ----')
#result = subtract_numbers(8, 3)
result = subtract_numbers(x=8, y=3)
print(result)

print('-- test multiply function ----')
#result = multiply_numbers(2, 2)
result = multiply_numbers(x=2, y=2)
print(result)

print('-- test divide function ----')
#result = divide_numbers(8, 0)
result = divide_numbers(x=8, y=0)
if result is not None:
    print(result)
