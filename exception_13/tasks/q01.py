def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print('Division by zero is not allowed')


v_result = divide_numbers(8, 0)
print(v_result)
