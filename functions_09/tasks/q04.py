print('---write a function get_max_num an min_num---')


def max_num(my_list):
    result = max(my_list)

    return result


def min_num(my_list):
    result = min(my_list)

    return result


list1 = [10, 20, 30, 40]
v_result = max_num(list1)
print('max_num = ', v_result)

list1 = [10, 20, 30, 40]
v_result = min_num(list1)
print('min_num = ', v_result)
