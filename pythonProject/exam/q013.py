print('Check if an element exists in a list in Python and return all occurrence indexes of the element in this list ')

def find_number(my_list, value):
    if value in my_list:
        return my_list.index(value)


list2 = [5, 6, 7, 8]
v_result = find_number(list2, 7)
print(v_result)
