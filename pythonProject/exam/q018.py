print('swap 2 numbers in a program without using a temporary variable ')

numbers_list = [10, 4, 5, 8]
numbers_list[0], numbers_list[-1] = numbers_list[-1], numbers_list[0]
print(numbers_list)
