
def calculate_average(num_list):
    try:
        total = 0
        for item in num_list:
            total = total+item
            average = total / len(num_list)
        return average
    except TypeError:
        print('Error: Non-numeric value found in the list!')


v_result = calculate_average([10, 20, '30z', 40])
print(v_result)

