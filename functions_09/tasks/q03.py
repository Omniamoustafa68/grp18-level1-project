print('--- write function sum_positive_numbers---')


def sum_positive_numbers(my_list):
    total = 0
    for item in my_list:
        if item > 0:
            total = total + item
    return total


def count_positive_numbers(my_list):
    count_positive = 0
    for item in my_list:
        if item > 0:
            count_positive = count_positive + 1
    return count_positive


list1 = [3, 6, -1, -4, 5]
v_result = sum_positive_numbers(list1)
print('sum numbers positive = ', v_result)


list1 = [3, 6, -1, -4, 5]
v_result = count_positive_numbers(list1)
print('count positive numbers = ', v_result)
