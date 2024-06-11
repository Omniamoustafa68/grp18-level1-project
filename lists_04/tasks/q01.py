print('--- program to calculate sum, count of even numbers, odd numbers ---')
numbers_list = [15, 16, 20, 3, 9, 20]

total_even, count_even, total_odd, count_odd = 0, 0, 0, 0
for item in numbers_list:
    if item % 2 == 0:
        total_even = total_even + item
        count_even = count_even + 1
    else:
        total_odd = total_odd + item
        count_odd = count_odd + 1

print(total_even, count_even, total_odd, count_odd)